# -*- coding: utf-8 -*-
"""
Created on Wed Nov 10 20:00:04 2021

@author: navar
"""

import pandas as pd

# Pandas mades it easy to turn a CSV into a dataframe, we just call read_csv()
df = pd.read_csv('C:/Users/navar/OneDrive/Documentos/Python Scripts/mpg_BDD.csv', index_col=("Unnamed: 0"))

# And let's look at the first few rows
df.head() #collez dans le workspace 

df_colonnes=df[['model', 'cyl']] # choisir multilpes colonnes 

df_copy=df[df['model']=='jetta'] #choisir où c'est égale à 'jetta'

df_query=df[(df['model']=='jetta') & (df['year']==2008)] #conditions multiples 

jetta_mean=df[(df['model']=='jetta')].mean() #conditions multiples 


total_km=0
for km in df_copy['cty']: # juste pour verifier si la commande precedente donnait vraiment la moyenne de le sous groupe 'jetta'
    total_km=total_km + km
    jettaMoy=total_km/len(df_copy['cty'])
    
    
audi_models=df.set_index(['manufacturer','model' ])

audi_models=audi_models.loc[[('audi', 'a4'), 
                            ('audi', 'a4 quattro'),
                            ('audi', 'a6 quattro')]]