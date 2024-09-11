# -*- coding: utf-8 -*-
"""
Created on Fri Oct 29 14:47:01 2021

@author: navar
"""



#-------------- Search sub-string; return index -----------------------




def word_search(doc_list, keyword):
    sublist=[];
    for i in range(len(doc_list)):
        doc_list_v1 = doc_list[i];
        doc_list_v2 = doc_list_v1.lower();
        doc_list_v3 = doc_list_v2.strip(",.");
        doc_list_v4 = doc_list_v3.split();
        sublist.append(i);
        for j in range(len(doc_list_v4)):  
            if  doc_list_v3[j]==keyword :
                return sublist.index(doc_list[i])
            
        return print("Element n'a pas été trouvé")
    
    
    
# doc_list.index(keyword.capitalize())