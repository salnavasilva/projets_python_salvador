# -*- coding: utf-8 -*-
"""
Created on Mon Nov 15 22:04:05 2021

@author: navar
"""

import pandas as pd ;
import numpy as np;
import scipy.stats as stats

BDD=pd.read_csv('C:/Users/navar/OneDrive/Documentos/Python Scripts/NISPUF17.csv', index_col=(0));
print(type(BDD));
print(np.shape(BDD));


CHKN_POX=BDD.loc[:, ['HAD_CPOX','P_NUMVRC']]
CHKN_POX=CHKN_POX[CHKN_POX['HAD_CPOX']<=2]
CHKN_POX=CHKN_POX.dropna(axis=0)

corr, pval=stats.pearsonr(CHKN_POX["HAD_CPOX"],CHKN_POX["P_NUMVRC"])

