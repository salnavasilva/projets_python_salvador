# -*- coding: utf-8 -*-
"""
Created on Sat Dec  4 17:04:33 2021

@author: navar
"""



import pandas as pd #read_html
import numpy as np
import html5lib
from clean_team_names import clean_team_names #removes additionnal arg. like : [block 1]
from team_separating_func import team_sep # separates instances such as : 'GiantsJets'
from get_team_name import city_team_sep # retieves the team name from the W/L% df

"""
D'abord on va importer le tableau qui se trouve sur wikipedia et 
contient les regions métropolitaines sportives de USA 

"""
# Population estimate table
html_BDDs = pd.io.html.read_html("file:///C:/Users/navar/OneDrive/Documentos/Python%20Scripts/Semaine4/wikipedia_data.html")

Metropol_BDD = html_BDDs[1]
Metropol_BDD = Metropol_BDD.iloc[:-1, [0,3,5,6,7,8]] # :-1 pour eviter la dernière ligne qui est la totale 
Metropol_BDD.replace(to_replace=r'—+', value='', regex=True, inplace = True)
# win/loss ratio tables for each sport
# ATTENTION : on utilise que les données pour le 2018 

NFootL_BDD = pd.read_csv(r'C:\Users\navar\OneDrive\Documentos\Python Scripts\Semaine4\nfl.csv', skiprows=[1,6,11,16,21,26,31,36])
NFootL_BDD = NFootL_BDD[NFootL_BDD['year']==2018]
#-----------------------------------------------------
NHL_BDD = pd.read_csv(r'C:\Users\navar\OneDrive\Documentos\Python Scripts\Semaine4\nhl.csv', skiprows=[1,10,19,27])
NHL_BDD = NHL_BDD[NHL_BDD['year']==2018]
#-----------------------------------------------------
MLB_BDD = pd.read_csv(r'C:\Users\navar\OneDrive\Documentos\Python Scripts\Semaine4\mlb.csv')
MLB_BDD = MLB_BDD[MLB_BDD['year']==2018]
#-----------------------------------------------------
NBA_BDD = pd.read_csv(r'C:\Users\navar\OneDrive\Documentos\Python Scripts\Semaine4\nba.csv')
NBA_BDD = NBA_BDD[NBA_BDD['year']==2018]


#------------------------Cleaning team names REGEX --------------------------
sports=['NFL', 'MLB', 'NBA', 'NHL'] #1èr For
sports_BDD=[NFootL_BDD, NHL_BDD, MLB_BDD, NBA_BDD] #2ème For

for sport in sports:
    clean_team_names(Metropol_BDD, sport )

for i in sports_BDD:
    clean_team_names(i)

# identifier les noms comme Giants/Jets et les separer et explode()

for sport in sports:
    team_sep(Metropol_BDD, sport )
    
Metropol_BDD.rename(columns={'Population (2016 est.)[8]':'Population'}, inplace=True) #changer le nom de la colonne


#------------------------Population df and W/L % ratio --------------------------
#Preparing for merge on team name


#///// NFL--------------------------------------------------------------------
#explode() 
popu_nfl=Metropol_BDD.loc[:,['Metropolitan area','Population','NFL']].explode('NFL')
#seperate the team name from the city et rendre plus precise la BDD NFootL
city_team_sep(NFootL_BDD) # already inserts fun results into df automat.
wl_nfl=NFootL_BDD.loc[:,['W-L%', 'team', 'year', 'name_teams']]
city_wl_nfl=pd.merge(left=popu_nfl, right=wl_nfl, how='inner', left_on='NFL', right_on='name_teams')

city_wl_nfl['Population'] = city_wl_nfl['Population'].astype('int64')
city_wl_nfl['W-L%'] = city_wl_nfl['W-L%'].astype('float64')
city_wl_nfl.set_index(keys='Metropolitan area', inplace=True)
city_wl_nfl = city_wl_nfl.groupby('Metropolitan area').agg({'W-L%':np.mean, 'Population': np.mean})


#///// MLB--------------------------------------------------------------------
popu_mlb=Metropol_BDD.loc[:,['Metropolitan area','Population','MLB']].explode('MLB')

city_team_sep(MLB_BDD)
MLB_BDD.loc[:, 'name_teams'].replace({'Sox':'Red Sox',
                                       'Jays':'Blue Jays'}, inplace=True)
#Replace duplicate 'Red Sox' with 'White Sox'
MLB_BDD.loc[8, 'name_teams']='White Sox'
wl_mlb=MLB_BDD.loc[: , ['W-L%', 'team', 'year', 'name_teams']] 
city_wl_mlb=pd.merge(left=popu_mlb, right=wl_mlb, how='inner', left_on='MLB', right_on='name_teams')
city_wl_mlb['Population'] = city_wl_mlb['Population'].astype('int64')

city_wl_mlb.set_index(keys='Metropolitan area', inplace=True)
city_wl_mlb = city_wl_mlb.groupby('Metropolitan area').agg({'W-L%':np.mean, 'Population': np.mean})


#///// NBA--------------------------------------------------------------------
popu_nba=Metropol_BDD.loc[:,['Metropolitan area','Population','NBA']].explode('NBA')

city_team_sep(NBA_BDD)
NBA_BDD.loc[:, 'name_teams'].replace({'Blazers':'Trail Blazers'}, inplace=True)
wl_nba=NBA_BDD.loc[:,['W/L%', 'team', 'year', 'name_teams']]
city_wl_nba=pd.merge(left=popu_nba, right=wl_nba, how='inner', left_on='NBA', right_on='name_teams')
city_wl_nba['Population'] = city_wl_nba['Population'].astype('int64')
city_wl_nba['W/L%'] = city_wl_nba['W/L%'].astype('float64')

city_wl_nba.set_index(keys='Metropolitan area', inplace=True)
city_wl_nba = city_wl_nba.groupby('Metropolitan area').agg({'W/L%':np.mean, 'Population': np.mean})


#///// NHL--------------------------------------------------------------------
popu_nhl=Metropol_BDD.loc[:,['Metropolitan area','Population','NHL']].explode('NHL')

city_team_sep(NHL_BDD)
#W/L% ratio = W/(W+L)
NHL_BDD['W']=NHL_BDD['W'].astype('int64')
NHL_BDD['L']=NHL_BDD['L'].astype('int64')
NHL_BDD['W-L%']= NHL_BDD.loc[:,'W']/(NHL_BDD.loc[:,'W']+NHL_BDD.loc[:,'L'])
#replace incomplete team names
NHL_BDD.loc[:, 'name_teams'].replace({'Leafs':'Maple Leafs',
                                      'Wings':'Red Wings',
                                      'Jackets':'Blue Jackets',
                                      'Knights':'Golden Knights'}, inplace=True)
wl_nhl=NHL_BDD.loc[:, ['W-L%', 'team', 'year', 'name_teams']]
city_wl_nhl=pd.merge(left=popu_nhl, right=wl_nhl, how='inner', left_on='NHL', right_on='name_teams')
city_wl_nhl['Population'] = city_wl_nhl['Population'].astype('int64')


city_wl_nhl.set_index(keys='Metropolitan area', inplace=True)
city_wl_nhl = city_wl_nhl.groupby('Metropolitan area').agg({'W-L%':np.mean, 'Population': np.mean})











