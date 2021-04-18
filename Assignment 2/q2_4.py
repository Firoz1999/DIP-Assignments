#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 18 01:33:39 2021

@author: vaibhav
"""

import cv2
import numpy as np
from q2_3 import fft
 
def dft_2D(image):
    res = []
    r,c=image.shape
    for i in range(r):
        res.append(fft(image[i]))
    
    for j in range(c):
        col = []
        for i in range(r):
            col.append(res[i][j])
        col = fft(col)
        for i in range(r):
            res[i][j] = col[i]
    return res
  
if __name__ == "__main__":
  image = './images/Lena.png'
  I = cv2.imread(image)
  I = cv2.cvtColor(I, cv2.COLOR_BGR2GRAY)
  arr=dft_2D(I)
  f = np.fft.fft2(I) 
  print(np.allclose(arr, f))