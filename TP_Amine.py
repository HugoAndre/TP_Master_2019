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
        print('bon nombre de chiffre.....vérification des conditions de Luhn....')
        return 1 
    
    D=S[0]


    if D==1:
        D=2
    elif D==2:
            D=4
    elif D==3:
            D=6
    elif D==4:
            D=8
    elif D==5:
            D=1
    elif D==6:
            D=3
    elif D==7:
            D=5
    elif D==8:
            D=7
    else:
         D=9
   
    
        

Reponse=verif()





#        for S in range (0,12):
#            S=S[] 
#    D=S[1][3][5][7][9][11]
   