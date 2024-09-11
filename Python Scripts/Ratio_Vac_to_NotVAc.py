# -*- coding: utf-8 -*-
"""
Created on Mon Nov 15 21:03:17 2021

@author: navar
"""

import pandas as pd ;
import numpy as np;

BDD=pd.read_csv('C:/Users/navar/OneDrive/Documentos/Python Scripts/NISPUF17.csv', index_col=(0));
print(type(BDD));
print(np.shape(BDD));


CHKN_POX=BDD.loc[:, ['SEX','HAD_CPOX','P_NUMVRC']]

HAD_CPOX_VAC=CHKN_POX[(CHKN_POX['P_NUMVRC']>=1) & (CHKN_POX['HAD_CPOX']==1)];

NO_CPOX_VAC=CHKN_POX[(CHKN_POX['P_NUMVRC']>=1) & (CHKN_POX['HAD_CPOX']==2)];


MALE_RATIO=len(HAD_CPOX_VAC[HAD_CPOX_VAC['SEX']==1])/len(NO_CPOX_VAC[NO_CPOX_VAC['SEX']==1]);

FEMALE_RATIO=len(HAD_CPOX_VAC[HAD_CPOX_VAC['SEX']==2])/len(NO_CPOX_VAC[NO_CPOX_VAC['SEX']==2]);

DICT= {"male":MALE_RATIO,
    "female":FEMALE_RATIO};

print(DICT);

