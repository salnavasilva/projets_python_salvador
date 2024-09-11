# -*- coding: utf-8 -*-
"""
Created on Wed Nov 24 16:54:53 2021

@author: navar
"""

import pandas as pd
import numpy as np
import re

Energy= pd.read_excel('C:/Users/navar/OneDrive/Documentos/Python Scripts/Energy Indicators.xls', skiprows=(17) )
Energy = Energy.iloc[:227,2:6] #Pour prendre seulement la partie qu'on veut

#Attribuer les noms des colonnes 
Energy.columns=['Country', 'Energy Supply', 'Energy Supply per Capita', '% Renewable'];

Energy.iloc[:, 1:4]=Energy.iloc[:, 1:4].apply(pd.to_numeric, errors='coerce')

#Convertir PetaJoules à GigJoules => 1*10^6 GJ/PJ
Energy.loc[:,'Energy Supply']=Energy.loc[:,'Energy Supply']*1000000



#Séparer les values de l'index dans  le Series (.values \ou .index)
CleanNames=(Energy['Country']).values
CleanNames= '\n'.join(CleanNames) # list to str
#Regex pour laisser les noms des pays sans chiffres ou characters aberrantes
CleanNames=re.sub("[0-9]*|\([^)]*\)",'', CleanNames) #re.sub() elimine ce qui est en parantheses (1ère argu.) et le remplace avec ce qui est dans le second argument
#Diviser le string créé précédement et le reinserer dans le DataFrame
CleanNames=CleanNames.split(sep=('\n'))
Energy['Country']=CleanNames


#Changer noms specifiques 
Energy.iloc[:,0].replace({"Republic of Korea": "South Korea",
"United States of America": "United States",
"United Kingdom of Great Britain and Northern Ireland": "United Kingdom",
"China, Hong Kong Special Administrative Region": "Hong Kong",
"Iran ": "Iran"}, inplace=True)

#------------------------------------    GDP    ------------------------------------------

#load the GDP data from the file assets/world_bank.csv

GDP=pd.read_csv('C:/Users/navar/OneDrive/Documentos/Python Scripts/world_bank.csv',header=4 )

GDP=GDP.rename(columns={'Country Name':'Country'})

#Changer noms specifiques
GDP.iloc[:,0].replace({"Korea, Rep.": "South Korea", 
"Iran, Islamic Rep.": "Iran",
"Hong Kong SAR, China": "Hong Kong"}, inplace=True)




#------------------------------------    ScimEn    ------------------------------------------

#Finally, load the Sciamgo Journal and Country Rank data for Energy Engineering and Power Technology from the file assets/scimagojr-3.xlsx,

ScimEn=pd.read_excel('C:/Users/navar/OneDrive/Documentos/Python Scripts/scimagojr-3.xlsx')


#---------------------------    élaboration de la BDD finale    ------------------------------------------

# 1. - Merge la BDD Scimen & Energy
Semi_merge=pd.merge(left=ScimEn.iloc[0:15,:], right=Energy, how='left', 
                    left_on='Country', right_on='Country')
# 2. - Merge la BDD Semi_merge et GDP

BDD_finale=pd.merge(left=Semi_merge, right=GDP.iloc[:,np.r_[0,50:60]], how='left',
             left_on='Country', right_on='Country')
BDD_finale.set_index(keys='Country', inplace=True)


#---------------------------    Données perdues    ------------------------------------------

Outer_Semi=pd.merge(left=ScimEn, right=Energy, how='outer', 
                    left_on='Country', right_on='Country')
Outer_BDD=pd.merge(left=Outer_Semi, right=GDP, how='outer',
             left_on='Country', right_on='Country')

Valeurs_totales=Outer_BDD['Country'].unique()

Valeurs_perdues=len(Valeurs_totales)-len(BDD_finale['Rank']) #'Rank' car on avait elimine la colonne country de BDD_finale mais c'est toujours de len==15


#------------------------------- QUESTION 3 ------------------------------

#Comment below est desormais faux
"""
On a fait une BDD complete parce avant je l'avais modifié d'un coup,
donc on peut pas utilise BDD_finale sinon BDD_complète

Semi_complete=pd.merge(left=ScimEn, right=Energy, how='left', 
                    left_on='Country', right_on='Country')
# 2. - Merge la BDD Semi_merge et GDP all dates 

BDD_complete=pd.merge(left=Semi_complete, right=GDP.iloc[:,np.r_[0,50:60]], how='left',
              left_on='Country', right_on='Country')
mean_GDP=BDD_complete.iloc[:,np.r_[1, 11:21]]
"""



def row_gdp_mean(df):
    
    
    """

    Parameters
    ----------
    df : TYPE DataFrame
        On utilise le DataFrame qu'on a obtenu après le merge.

    Returns
    -------
    lst : TYPE liste
        retourne le GDP moyenne de chqaue 15 pays.

    """
    lst=[]
    for i in BDD_finale.index:
        row_avg = df.loc[i,'2006':'2015'].mean();
        lst.append(row_avg)
        
    return lst



Series_GDP=pd.Series(data=row_gdp_mean(BDD_finale), index=BDD_finale.index)
Series_GDP.sort_values(axis=0, ascending=False, inplace=True)
avgGDP=Series_GDP.nlargest(15)


#------------------------------- QUESTION 4 ------------------------------


"""

#Pour se debarraser du préavis : 
    
A value is trying to be set on a copy of a slice from a DataFrame.
Try using .loc[row_indexer,col_indexer] = value instead

Cela s'affiche parce qu'on modifie la BDD original deux fois, 
donc on dois faire une copie pour ne pas faire de modifications inplace

UTILISE : df2=df.copy()

"""    


#Changement en GDP MOYEN du #6ème (uk) pays le plus grand au fil du 10 dernieres années

Delta_Pays=(BDD_finale.loc['United Kingdom','2015']-BDD_finale.loc['United Kingdom','2006'])


#------------------------------- QUESTION 5 ------------------------------

""" Apparemment on doit utiliser BDD 1 (BDD finale pour les question 3 - 13)
"""

Moy_energy_pc=BDD_finale.agg({'Energy Supply per Capita':np.nanmean})[0] #pour retourner que la valeur 

#------------------------------- QUESTION 6 ------------------------------

#Tuple du pays avec la plus grande consomation d'energie renovable  %

Max_renew=BDD_finale.nlargest(1, '% Renewable')

Max_renew_tuple=(Max_renew.index[0], Max_renew.loc['Brazil','% Renewable'])

#------------------------------- QUESTION 7 ------------------------------

#RatioCitation = Self-Citations / Total Citations

#Quel pays a le plus grand Ratio?

Self_citations = BDD_finale.loc[:,'Self-citations']
Total_citations = BDD_finale.loc[:,'Citations'] 


BDD_finale['Ratio']=Self_citations/Total_citations



RatioMax = BDD_finale.nlargest(1, 'Ratio')
RatioMax_tupple=(RatioMax.index[0] , RatioMax.loc['China','Ratio'])


#------------------------------- QUESTION 8 ------------------------------

#Pour laisser la BDD_finale dans sa forme originale; ce qui ne serait pas necessaire si j'avais fais comme ce qui est en bas
BDD_finale.drop('Ratio', axis=1, inplace=True)

Pop_estime=BDD_finale.loc[:,'Energy Supply']/BDD_finale.loc[:,'Energy Supply per Capita']
Pop_estime.rename('Population', inplace=True)

#Retourne que le nom du 3ème pays le plus grande en termes de population
Country_3=Pop_estime.nlargest(3).index[2]

#------------------------------- QUESTION 9 ------------------------------

import matplotlib.pyplot as plt

Citable_docs_per_capita = BDD_finale.loc[:,'Citable documents']/Pop_estime

PearsonsCorr=Citable_docs_per_capita.corr(BDD_finale.loc[:,'Energy Supply per Capita'], method = 'pearson')


# plt.scatter(x=Citable_docs_per_capita, y=BDD_finale.loc[:,'Energy Supply per Capita'], marker='o')
# plt.xlabel('Citable Documents per Capita')
# plt.ylabel('Energy suppy per Capita')
#plt.show()



#------------------------------- QUESTION 10 ------------------------------

Renewable_mediane = np.nanmedian(BDD_finale.loc[:, '% Renewable'])



def HighRenew(df):
    lst=[];
    
    for i in BDD_finale.index:
        if df.loc[i, '% Renewable'] > Renewable_mediane:
            lst.append(1)
        elif df.loc[i, '% Renewable'] < Renewable_mediane:
            lst.append(0) 
        else:
            lst.append(1)
            
    return lst
    
HighRenew_series = pd.Series(data= HighRenew(BDD_finale), index=BDD_finale.sort_values(by='Rank', axis=0, ascending=True).index) 

#------------------------------- QUESTION 11 ------------------------------
"""

Dans cette section j'avais besion de faire un  Multi index 
Je laisse donc tout ce que j'ai fait sur les df's Multi index pour toute eventuelle référence
"""
ContinentDict  = {'China':'Asia', 
                  'United States':'North America', 
                  'Japan':'Asia', 
                  'United Kingdom':'Europe', 
                  'Russian Federation':'Europe', 
                  'Canada':'North America', 
                  'Germany':'Europe', 
                  'India':'Asia',
                  'France':'Europe', 
                  'South Korea':'Asia', 
                  'Italy':'Europe', 
                  'Spain':'Europe', 
                  'Iran':'Asia',
                  'Australia':'Australia', 
                  'Brazil':'South America'}


BDD_Continent=pd.DataFrame(ContinentDict.items(), 
                           columns=['Country','Continent'])

BDD_Continent['Population']=Pop_estime.values


#Multi-index for BDD

BDD_Continent.set_index(['Continent', 'Country'], drop=True, inplace=True)

BDD_Continent.sort_index(level=['Continent','Country'],inplace=True)

#BDD_Continent.to_csv(r'C:\Users\navar\OneDrive\Documentos\Python Scripts\ContinentBDD.csv')

"""
return a DataFrame with index named Continent 
['Asia', 'Australia', 'Europe', 'North America', 'South America'] 
and columns ['size', 'sum', 'mean', 'std']
"""


# Getting only the unique() continent values to be the first column of our new df
continentStat=pd.DataFrame(BDD_Continent.index.get_level_values('Continent').unique(), 
                           columns=['Continent'])

# stats of df : BDD_Continent 
#from Continent col. ['size'] 
#and from Population column ['sum', 'mean', 'std']

#size
continentStat['size']=BDD_Continent.groupby(['Continent']).count().values

#sum pop
continentStat['sum']=BDD_Continent.groupby(['Continent'])['Population'].sum().values

# mean pop
continentStat['mean']=BDD_Continent.groupby(['Continent'])['Population'].mean().values

# std pop
continentStat['std']=BDD_Continent.groupby(['Continent'])['Population'].std().values

continentStat.set_index('Continent', drop=True, inplace=True)


#------------------------------- QUESTION 12 ------------------------------


bin_renewable=BDD_finale.copy()

# couper en 5 bins differents et equitablement distribués
#Categories (5, interval[float64]): [(2.212, 15.753] < (15.753, 29.227] < (29.227, 42.701] <
#                                    (42.701, 56.174] < (56.174, 69.648]]

bin_renewable['% Renewable']=pd.cut(BDD_finale['% Renewable'], bins = 5, labels=('1','2','3','4','5'))
#réinitialiser les indices --> vers index patr défaut
bin_renewable.reset_index(inplace=True)
#creation de la trame de la BDD 
continent_renewable=pd.DataFrame(ContinentDict.items(), 
                           columns=['Country','Continent'])
# union des deux bases
BDD_renewable=pd.merge(left=continent_renewable, 
                       right=bin_renewable.loc[:,['Country','% Renewable']], 
                       how='inner', 
                       left_on='Country',
                       right_on='Country')
# création de l'indice multi Index
BDD_renewable.set_index(keys=['Continent','% Renewable'], drop=True, inplace=True)
BDD_renewable.sort_index(level=['Continent', '% Renewable'],inplace=True)
# pour indiquer co,bien de pays apartiennent à chaque bin
BDD_renewable=BDD_renewable.groupby(['Continent', '% Renewable'])['Country'].count()
# éliminer les bins où il n'y a pas de pays
BDD_renewable=BDD_renewable[BDD_renewable.iloc[:]!=0]

#------------------------------- QUESTION 13 ------------------------------

Pop_estime

def num_to_str(series):
    series_lst=[];
    for i in range(0, len(series)):
        num_str=("{:,.8f}".format(series[i]))
        series_lst.append(num_str)
    return series_lst
        
PopEst=pd.Series(data=num_to_str(Pop_estime), index=Pop_estime.index)
        










