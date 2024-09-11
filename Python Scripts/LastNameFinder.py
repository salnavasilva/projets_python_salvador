# -*- coding: utf-8 -*-
"""
Created on Fri Nov  5 19:59:34 2021

@author: navar

En gros, dans ce script je prends le dernier element de chaque string dans 
la list 'people' et je le concatene avec Dr.{} pour obtenir :
    
Dr. Brooks
Dr. Collins-Thompson
Dr. Vinod
Dr. Romero

"""

people = ['Dr. Christopher Brooks', 
          'Dr. Kevyn Collins-Thompson', 
          'Dr. VG Vinod Vydiswaran', 'Dr. Daniel Romero'];


lastNames=[];

for i in range(len(people)):
    
    lastNames.append(people[i].split()[-2])
    
    print('Dr. {}'.format(lastNames[i]))
    
    