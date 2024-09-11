# -*- coding: utf-8 -*-
"""
Created on Wed Nov 24 09:55:41 2021

@author: navar
"""
import pandas as pd 
import numpy as np
import random

times=['1996-24-07', '09/06/1976', '24.07.2010']


#/ pd.to_datetime rendre de une manière standard tous les formats de date 
times=pd.to_datetime(times, dayfirst=True)

delta=(times[0]- times[1])

dates=pd.date_range(start='01/01/2021', end='31/12/2021', freq='D')

mesures=pd.DataFrame(np.random.randint(-100,101, (365,2)), 
                     index=dates, columns=(['X1', 'X2']))

delta_mes=mesures.diff()

np.unique(mesures, return_counts=1) #returns number of instances of a unique value is in th DF