# -*- coding: utf-8 -*-
"""
Created on Wed Dec 15 21:00:24 2021

@author: navar
"""

import pandas as pd
s1=pd.Series(data=[20,15,18,31], index=['Mango', 'Strawberry', 'Blueberry', 'Vanilla'])
s2=pd.Series(data=[20,30,15,20,20],index=['Strawberry', 'Vanilla', 'Banana', 'Mango', 'Plain'] )

s3=s1.add(s2)

s4=s1.add(s2, fill_value=0)
