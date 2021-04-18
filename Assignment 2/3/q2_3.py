#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 18 15:56:47 2021

@author: vaibhav
"""
from cmath import exp, pi
import numpy as np

def fft(x):
  
    n=len(x)
    if(n<=1):
        return x
    
    even= fft(x[0::2])
    odd = fft(x[1::2])
    
    T = []
    for k in range(n//2):
        T.append(exp(-2j*pi*k/n)*odd[k])
        
    left = []
    right = []
    for k in range(n//2):
        left.append(even[k] + T[k])
        right.append(even[k] - T[k])
    
    return left + right


if __name__ == "__main__":
  x=np.array([2,4,6,8,1,2])   
  print(fft(x))
  print(np.allclose(fft(x), np.fft.fft(x)))
