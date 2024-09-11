# -*- coding: utf-8 -*-
"""
Created on Sat Nov 20 17:30:16 2021

@author: navar
"""

import pandas as pd
import numpy as np



    
df=pd.read_excel('C:/Users/navar/OneDrive/Documentos/Python Scripts/college_scorecard.xlsx')
# Set index et comme ça on evite de passer un argumment quand on invoque la fonction = rank_university()


transformed_df=df;

def rank_university(item):
   
   if item<=100:
       return 'First Tier Top University'
   elif item>100 and item<=200:
       return 'Second Tier Top University'
   elif item>200 and item<=300:
       return 'Third Tier Top University'
   else:
       return 'Other Tier Top University'


    
transformed_df['rank_level']=df['world_rank'].apply(lambda x : rank_university(x))


#columns=pd.DataFrame(columns=df.columns)
uni=df.groupby(['institution', 'year'])['publications'].unique()

# pivot table 

pivot=df.pivot_table(values='publications', index='institution', 
                     columns='year', aggfunc=(np.sum),
                     margins=True)

#Stack and unstack
stack_pivot=pivot.stack()
unstacked_pivot=pivot.unstack()





#df=df.set_index('world_rank')
# def rank_university(item):
    
#     if item<=100:
#         return str('First Tier Top University')
#     if item>=101 & item<=200:
#         return str('Second Tier Top University')
#     if item>=201 & item<=300:
#         return str('Third Tier Top University')
#     else:
#         return 'Other Tier Top University'
# for group, frame in df.groupby(rank_university): 
#     print(group)