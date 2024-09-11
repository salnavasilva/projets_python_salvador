# -*- coding: utf-8 -*-
"""
Created on Thu Oct 28 14:19:18 2021

@author: navar
"""
from has_lucky_number import has_lucky_number;
import random as rd;

results=[];
IsLucky=[];


results.append([round(1+rd.random()*(1000-1)) for i in range(100)])


for k in range(100):
    IsLucky.append(has_lucky_number(results[:k]));
