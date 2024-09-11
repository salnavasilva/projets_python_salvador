# -*- coding: utf-8 -*-
"""
Created on Wed Dec 15 20:26:32 2021

@author: navar
"""
def char_spotter():
    import re
    
    s = 'ACAABAACAAABACDBADDDFSDDDFFSSSASDAFAAACBAAAFASD'
    
    result = []
    # compete the pattern below
    pattern = """(?P<precedingchar>([B-Z]{1})) #Character precding the triple AAA
    ([A]{3})
    """ 
    for item in re.finditer(pattern, s, re.VERBOSE):
      # identify the group number below.
      result.append(item.group()[0])
    return result
  
  