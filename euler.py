# -*- coding: utf-8 -*-
"""
Created on Tue Nov 26 21:43:53 2019

@author: mathi
"""

import numpy as np
import matplotlib.pyplot as plt

# Euler method
def euler(f,y0,a,b,h):
    l = []
    t,y = a,y0
    
    while t <= b:
        l.append(y)
        t += h
        y += h * f(t,y)
        
    plt.plot(l)
    plt.ylim(ymin=0)
    plt.grid()
    plt.show()
 
def func(t, y):
	return 0.04*y*(1-y/100)
 
euler(func,20,0,240,12)