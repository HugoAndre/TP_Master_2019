# -*- coding: utf-8 -*-
"""
Created on Mon Nov 18 11:48:16 2019

@author: Amine
"""
def verif():
    
    S=input('entrer le code de votre carte ?')
    X=len(S)
    
    if X!=12:
        print ('code carte faux')
        return 0
    else:
        print('bon nombre')
        return 1
    
Reponse=verif()
 #        for S in range (0,12):
#            S=S[] 
    