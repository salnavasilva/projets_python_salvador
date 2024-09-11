# -*- coding: utf-8 -*-
"""
Created on Thu Oct 28 14:04:38 2021

@author: navar
"""
import random 



def has_lucky_number(nums):
    """Return whether the given list of numbers is lucky. A lucky list contains
    at least one number divisible by 7.
    """
    for num in nums:
        if num % 7 == 0:
            return True
        else:
            return False
        
