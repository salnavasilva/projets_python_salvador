# -*- coding: utf-8 -*-
"""
Created on Thu Dec  9 18:35:14 2021

@author: navar
"""

def city_team_sep(df, team_col='team'):
    
    lst_cityteams=df[team_col].values;
    lst_cty=[];
    lst_teams=[];
    name=0;
    for name in range(0,len(lst_cityteams)):
        lst_teams.append(lst_cityteams[name].split()[-1])
        
        lst_cty.append(lst_cityteams[name].split()[0])
        
    df['name_teams']=lst_teams        
        
    return

        

   