# -*- coding: utf-8 -*-
"""
Created on Tue Nov  9 13:16:20 2021

@author: navar
"""

import pandas as pd
import numpy as np
import random

numbers=pd.Series(np.random.randint(0,10,1000))

second_numbers=numbers.mean()

for num in numbers:
    total=numbers.sum()
    mean=total/len(numbers)
    

    
x=np.arange(1000,5500,500)