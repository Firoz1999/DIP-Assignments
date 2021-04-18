#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 18 20:54:35 2021

@author: vaibhav
"""

import numpy as np
from q2_5 import dft2_phase_mag
import matplotlib.pyplot as plt
from cmath import exp,pi

def ifft(x):
    n=len(x)
    if(n<=1):
        return x
    
    even= ifft(x[0::2])
    odd = ifft(x[1::2])
    
    T = []
    for k in range(n//2):
        T.append(exp(2j*pi*k/n)*odd[k])
        
    left = []
    right = []
    for k in range(n//2):
        left.append(even[k] + T[k])
        right.append(even[k] - T[k])
        
    return left + right
  
  
def ifft2(image):
    res = []
    
    for i in range(len(image)):
        res.append(ifft(image[i]))
        
    for i in range(len(res[0])):
        col = []
        for j in range(len(res)):
            col.append(res[j][i])
        col = ifft(col)
        
        for j in range(len(res)):
            res[j][i]=col[j]
            
    res = np.absolute(res)
    
    return res

lena_mag,lena_phase,dog_mag,dog_phase=dft2_phase_mag()

ans = [[0 for i in range(512)] for j in range(512)]

for i in range(512):
  for j in range(512):
    ans[i][j] = lena_mag[i][j]*exp(1j*dog_phase[i][j])
      
result = ifft2(ans)
  
plt.imshow(result, cmap="gray")
title="Magnitude Lena,Phase Dog"
plt.title(title)
plt.show()

      

  

