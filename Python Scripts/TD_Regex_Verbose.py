# -*- coding: utf-8 -*-
"""
Created on Mon Nov  8 19:09:51 2021

@author: navar
"""

import re
def logs():
     
    with open('logWeb.txt', 'r') as file:
        log = file.read()
    #([0-9]{1,3}\.[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3})
    lst=[];
    pattern="""
    (?P<host>([0-9]{1,3}\.[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}))  #Host I.P. adress
    (\s\-\s) # tiret qui separe 
    (?P<user_name>[-]?[\w]*) #user name '-' tiret si ce n'est pas declaré c'est pour ça qu'on a mis * pour montrer soit l'identifiant ou soit rester avec le tiret seul
    (\s\[) #space
    (?P<time>.*) # Comme dans le time il y a plein de caracteres, ont peuven s'en servir de .+ pour tous et \[\] pour les crochet
    (\]\s\")
    (?P<request>.*) #idem qu'avant
    (\")
    """
        
    for item in re.finditer(pattern, log, re.VERBOSE):
        
        lst.append(item.groupdict())
        
    return lst
        
    
     
x=logs()    


