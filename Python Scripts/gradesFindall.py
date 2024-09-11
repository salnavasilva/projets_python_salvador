# -*- coding: utf-8 -*-
"""
Created on Mon Nov  8 17:00:14 2021

@author: navar
"""


import re

with open ('C:/Users/USNA0501/OneDrive - Savencia/Documents/Python Scripts/grades.txt', 'r') as file: #Deux arguments (file , mode) mode peut-être soit 'r' for read only soit 'w' for write c-à-d tu as l'intention de modifier
    grades=file.read()
    lst=[];
#regex='[A-Za-z]+[\s][A-Za-z]+.*[B]+'; # trouve toutes les instances de notes == B
# pattern="""
#     (?P<names>.*)
#     (\: )
#     (B)
#     """
for item in re.finditer("(?P<names>.*)(\: B)", grades):
    lst.append(item.group('names'))
print(lst)
    