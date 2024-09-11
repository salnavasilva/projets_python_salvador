# -*- coding: utf-8 -*-
"""
Created on Sat Nov 13 19:37:29 2021

@author: navar
"""

import pandas as pd 
import numpy as np
BDD=pd.read_csv('C:/Users/navar/OneDrive/Documentos/Python Scripts/NISPUF17.csv', index_col=(0));
print(type(BDD))
print(np.shape(BDD));
    
EDUC1=BDD.loc[:,'EDUC1'];

def proportion_de_education():
    
    
    EDUC1=BDD.loc[:,'EDUC1'];
    
    Mere_total=len(EDUC1);
    
    Sans_Bac=EDUC1[EDUC1==1]/len(EDUC1);
    Avec_Bac=EDUC1[EDUC1==2];
    Sans_Diplome=EDUC1[EDUC1==3];
    Avec_Diplome=EDUC1[EDUC1==4];
    
    #   
    Prop_Sans_Bac=len(Sans_Bac)/Mere_total;
    Prop_Avec_Bac=len(Avec_Bac)/Mere_total;
    Prop_Sans_Diplome=len(Sans_Diplome)/Mere_total;
    Prop_Avec_Diplome=len(Avec_Diplome)/Mere_total;
    
    Dict={"less than high school":Prop_Sans_Bac,
    "high school":Prop_Avec_Bac,
    "more than high school but not college":Prop_Sans_Diplome,
    "college":Prop_Avec_Diplome};
    
    return Dict
