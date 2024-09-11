# -*- coding: utf-8 -*-
"""
Created on Thu Apr 18 11:20:05 2024

@author: USNA0501
"""

import pandas as pd
 
# creating a DataFrame
list = [['Anton Yelchin', 36, 75.2, 54280.20],
        ['Yul Brynner', 38, 74.32, 34280.30],
        ['Lev Gorn', 31, 70.56, 84280.50],
        ['Alexander Godunov', 34, 80.30, 44280.80],
        ['Oleg Taktarov', 40, 100.03, 45280.30],
        ['Dmitriy Pevtsov', 33, 72.99, 70280.25],
        ['Alexander Petrov', 42, 85.84, 25280.75]]
df = pd.DataFrame(list, columns=['Name', 'Age', 'Weight', 'Salary'])



# converting 'Weight' from float to int
df['Weight'] = df['Weight'].astype(int)

# displaying the datatypes
print(df)

''' En appliquant .astype(int) sur la colonne weight on perd de l'information; on garde que la partie entière du float'''