# -*- coding: utf-8 -*-
"""
Created on Sat Dec  4 21:29:28 2021

@author: navar
"""

def clean_team_names(df, team_col_nom='team'):
    
   
    """
    im

    Parameters
    ----------
    df : TYPE = DataFrame
        DESCRIPTION : dataframe which contains a column of team names
    team_col_nom : TYPE = String, optional if choosing a 'BIG 4' df
        DESCRIPTION : The default is 'team'.
            **Remember to pass the colomn name as a str object**
    Returns
    -------
    None.

    """
    import re
    
    lst_teams = df[team_col_nom].values
    str_teams = '\n'.join(lst_teams)
    clean_teams=re.sub("\*|\+|\([^)]*\)|\[[^]]*\]",'', str_teams)
    clean_teams=clean_teams.split(sep=('\n'),)
    df[team_col_nom]=clean_teams
    
    return df









