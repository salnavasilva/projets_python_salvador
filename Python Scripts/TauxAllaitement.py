# -*- coding: utf-8 -*-
"""
Created on Sun Nov 14 22:14:48 2021

@author: navar
"""
import pandas as pd 
import numpy as np

BDD=pd.read_csv('C:/Users/navar/OneDrive/Documentos/Python Scripts/NISPUF17.csv', index_col=(0));
print(type(BDD))
print(np.shape(BDD));