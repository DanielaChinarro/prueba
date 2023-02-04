# -*- coding: utf-8 -*-
"""
Created on Tue Nov 29 21:37:21 2022

@author: prestamo
"""
"""EJERCICIO 6: tema 4"""

def polinomio(x,coef):
    w = len(coef)
    p=0
    for i in range(w):
        p +=coef[i]*x**i
        # f=f+(i*(a**b.index(i)))
    
    return p

print(polinomio(2,[1,0,1]))





