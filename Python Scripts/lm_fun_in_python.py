# -*- coding: utf-8 -*-
"""
Created on Fri Jan  5 10:57:11 2024

@author: USNA0501
"""

import numpy as np
import matplotlib.pyplot as plt
 
x = np.array([1, 2, 3, 4, 5])
y = np.array([3, 5, 7, 9, 11])
 
coefficients = np.polyfit(x, y, deg=1)

plt.plot(x,y)