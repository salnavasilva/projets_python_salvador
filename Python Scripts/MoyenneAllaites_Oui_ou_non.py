# -*- coding: utf-8 -*-
"""
Created on Mon Nov 15 17:33:57 2021

@author: navar
"""

import pandas as pd ;
import numpy as np;



BDD=pd.read_csv('C:/Users/navar/OneDrive/Documentos/Python Scripts/NISPUF17.csv', index_col=(0));
print(type(BDD));
print(np.shape(BDD));

H1N1_BDD=BDD.loc[:,['CBF_01','P_NUMFLU']];

allaites_oui=H1N1_BDD[(H1N1_BDD['CBF_01']==1)];
allaites_non=H1N1_BDD[(H1N1_BDD['CBF_01']==2)];

Moy_vac_allaites=allaites_oui.loc[:,'P_NUMFLU'].mean()
Moy_vac_NON_allaites=allaites_non.loc[:,'P_NUMFLU'].mean()

tuple1=(Moy_vac_allaites, Moy_vac_NON_allaites);

