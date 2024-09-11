# -*- coding: utf-8 -*-
"""
Created on Fri Nov  5 21:27:10 2021

@author: navar
"""

import numpy as np;

lowercase = 'abcdefghijklmnopqrstuvwxyz'
digits = '0123456789'

serial_num=[];

serial_num=[i+j+k+h for i in lowercase for j in lowercase for k in digits for h in digits]


serial_array=np.array(serial_num);

reshapeData=np.reshape(serial_array, (6760,10));


Slice_reshapeData=reshapeData[:2,:2];

Slice_reshapeData[0,0]=50;