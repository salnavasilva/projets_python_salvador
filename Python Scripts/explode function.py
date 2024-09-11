# -*- coding: utf-8 -*-
"""
Created on Thu Dec  9 17:11:42 2021

@author: navar
"""
import pandas as pd
import random
import numpy as np
df=pd.DataFrame(data=[np.random.random(10)*10 for x in range(10)])
df=df.round(0)


df[2]=df[2].astype(object)
df.at[2,2]=['A','B']
df2=df.copy()
df=df.explode(2)