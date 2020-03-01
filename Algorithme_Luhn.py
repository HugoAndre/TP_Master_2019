# -*- coding: utf-8 -*-
"""
Created on Sun Mar  1 15:43:57 2020

@author: Amine
"""
#Déclaration de la fonction de vérification de la condition de Luhn
def Luhn_condition():
#entrer le numéro de la carte bancaire 
    CB=input('Numéro CB: ')    
#initialiser les variables 
    list_provisoire = []
    Luhn_num = []
    var_provisoire = 0     
    for i in CB:
            i = int(i)                 
            if i%2 == 0:
                list_provisoire.append(str(i*2))
            else:
                list_provisoire.append(str(i))     
    for elem in list_provisoire:         
        if int(elem) >= 10:
            for j in elem:
                var_provisoire += int(j)
            Luhn_num.append(var_provisoire)
            var_provisoire = 0
        else:
            Luhn_num.append(int(elem))     
    for i in Luhn_num:
        var_provisoire += i    
    if var_provisoire % 10 == 0:
        print("Le code est bon")
    else:
        print("le code n'est pas bon")       
    print('Votre numéro de Luhn: ', Luhn_num)    
    if len(CB)==16:       
        return 'la taille de la carte est bonne'
    else:
        return 'Le code de votre carte doit contenir 16 chiffres'        
#Faire appel à la fonction de vérification de la condition de Luhn
result=Luhn_condition()
print(result)
