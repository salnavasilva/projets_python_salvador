# -*- coding: utf-8 -*-
"""
Created on Mon Nov  8 16:41:21 2021

@author: navar
"""

import re

def names():
    simple_string = """Amy is 5 years old, and her sister Mary is 2 years old. 
    Ruth and Peter, their parents, have 3 kids."""

    regex='[A-Z][a-z]+.?,?\s'
    match=re.findall(regex, simple_string);
    
    return match

