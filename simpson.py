# -*- coding: utf-8 -*-
"""
Created on Mon Oct 28 13:02:39 2019

@author: mathi
"""

import numpy as np

# Simpson's rule
def simpson (f, a, b, N=50):
        
        h=(b-a)/N
        
        x = np.linspace(a,b,N+1)
        y = f(x)
        
        I = h/3*np.sum(y[0:-1:2] + 4*y[1::2] + y[2::2])
        
        return I


print(simpson(lambda x: x**2, 0, 10))