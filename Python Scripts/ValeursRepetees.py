# -*- coding: utf-8 -*-
"""
Created on Fri Oct 29 14:07:57 2021

@author: navar
"""

meals = ['a', 'b', 'c', 'v', 'e', 'f', 'g',  'h', 'i', 'j', 'j' ];


def is_boring(meals):
    for i in range(0, len(meals)-1):
        if meals[i]==meals[i+1]:
            return True
         
    return False