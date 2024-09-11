# -*- coding: utf-8 -*-
"""
Created on Sun Nov  7 19:01:17 2021

@author: navar
"""

import re;

text="""Bonjour, je suis Salvador Navarro le MEXICAIN, Mexicain,
 mexicaine... ou MX1996"""

print(re.search("""1996$""", text))