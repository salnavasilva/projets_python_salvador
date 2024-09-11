# -*- coding: utf-8 -*-
"""
Created on Fri Dec  3 20:19:18 2021

@author: navar
"""

import pandas as pd
import numpy as np


BDDgrades = pd.read_csv(r'C:\Users\navar\OneDrive\Documentos\Python Scripts\grades.csv')
early_finishers = BDDgrades[pd.to_datetime(BDDgrades['assignment1_submission'])<'2016']
late_finishers = BDDgrades[pd.to_datetime(BDDgrades['assignment1_submission'])>'2016']