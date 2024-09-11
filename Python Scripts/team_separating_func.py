# -*- coding: utf-8 -*-
"""
Created on Sat Dec 11 20:06:02 2021

@author: navar
"""

def team_sep(df, col_name):
    """
    

    Parameters
    ----------
    df : BDD contenant la coonne 'team' d'un sport quelconque (dans ce cas-ci Metropol_BDD)
        DESCRIPTION : On introduit une colonne d'équipes qui sont parfois collés
        par exemple : 'GiantsJets' et de cela on va séparer et explode() pour rajouter 
        l'équipe supplementaire dans une nouvelle ligne 
        
    col_name : est l'un de 4 sports inclut dans Metropol_BDD
                NFL, NHL, MLB, NBA.

    Returns
    -------
    La bonne colonne 'teams' dans sa base originale.

    """
    import re
    # team_lst_col=df[col_name].values
    # str_teams="\n".join(team_lst_col)
    #Ici on identifie les equipes collés
    
    
    
    # clumped_teams=re.findall('(([A-Z][a-z]*)|([\d]+[a-z]*))[A-Z]{1}[a-z]*', str_teams)
    clumped_teams=df[df[col_name].str.contains(pat="(([A-Z][a-z]*)|([\d]+[a-z]*))[A-Z]{1}[a-z]*", regex=True)].index
    team_lst_col=df.loc[clumped_teams.values, col_name].values
    str_teams="\n".join(team_lst_col)
    separated_teams = re.findall(r'[A-Z][a-z]+ .*|[A-Z][a-z]+|[\d]+[a-z]+', str_teams)
    
    
    #return separated_teams dans la même ligne

    if col_name=='MLB':
        df[col_name] = df[col_name].astype(object)
        
        for i, j in zip(range(0, len(clumped_teams)), range(2,10,2)):
                df.loc[i, col_name] = separated_teams[i*2:j]
                
    elif col_name=='NBA':
        df[col_name] = df[col_name].astype(object)
        
        for i, j in zip(range(0, len(clumped_teams)), range(2,6,2)):
                df.loc[i, col_name] = separated_teams[i*2:j]
                
    elif col_name=='NFL':
        df[col_name] = df[col_name].astype(object)
        
        for i, j in zip(range(0, len(clumped_teams)), range(2,8,2)):
                df.loc[i, col_name] = separated_teams[i*2:j]
    
    elif col_name=='NHL':
        df[col_name] = df[col_name].astype(object)
        df.loc[0, col_name]=separated_teams[0:3]
        df.loc[1, col_name]=separated_teams[3:6]
    
    return df
            
        
        
        
        
    
    
    
    
    
    
    
    
    
    