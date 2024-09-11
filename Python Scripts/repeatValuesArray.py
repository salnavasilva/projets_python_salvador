# -*- coding: utf-8 -*-
"""
Created on Sat Nov  6 19:35:33 2021

@author: navar
"""

import numpy as np

lettres='abcdefghijklmnopqrstuvwxyz';
lettres=list(lettres); #utilisez une liste pour separer les valeurs du string



alphabetArray=[];
alphabetArray=[lettres for i in range(50) ];

alphabetArray=np.array(alphabetArray);

Sub_alpha=alphabetArray[:, [0,2,4]] # These indexs are inclusive apparement

