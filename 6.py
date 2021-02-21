#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 21 15:44:06 2021

@author: firoz
"""

import cv2
import numpy as np
import matplotlib.pyplot as plt

#fig,axs=plt.subplots(1,3)
def Histogram_equalization():
    img=np.array(cv2.imread("pout-dark.jpg",0))
    cv2.imshow('Original image',img)
    plt.hist(img.flatten(),bins=256,label='Original image Histogram',alpha=0.7)
    
    hist=np.zeros(256)
    for pixel in img.flatten():
        hist[pixel]+=1
        
    pmf=np.zeros(256)
    cmf=np.zeros(256)
    for i in range(256):
        pmf[i]=hist[i]/(len(img)*len(img[0]))
        
    for i in range(256):
        if(i==0):
            cmf[i]=pmf[i]
        else:
            cmf[i]=cmf[i-1]+pmf[i]
            
    cmf=cmf*255
    for i in range(256):
        cmf[i]=round(cmf[i])
        
    for i in range(len(img)):
        for j in range(len(img[0])):
            img[i][j]=cmf[int(img[i][j])]
    
    plt.hist(img.flatten(),bins=256,label='Histogram Equalized',alpha=0.7)
    cv2.imshow('Histogram Equalized Image',img)
    
    
Histogram_equalization()    
plt.legend()
plt.show()
    


