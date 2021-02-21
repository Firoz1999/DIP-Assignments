#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 21 19:14:08 2021

@author: firoz
"""

import cv2
import matplotlib.pyplot as plt
import numpy as np
#fig,axs=plt.subplots(1,3)

def Histogram_matching():
    img1=cv2.imread('pout-dark.jpg',0)
    cv2.imshow('Original Image',img1)
    plt.hist(img1.flatten(),bins=256,label='Original Image Histogram',alpha=0.5)
    
    img2=cv2.imread('pout-bright.jpg',0)
    cv2.imshow('Target Image',img2)
    plt.hist(img2.flatten(),bins=256,label='Target Image Histogram',alpha=0.5)
    
    hist1,hist2=np.zeros(256),np.zeros(256)
    for px1 in img1.flatten():
        hist1[px1]+=1
    for px2 in img2.flatten():
        hist2[px2]+=1
        
    eq_hist1,eq_hist2=np.zeros(256),np.zeros(256)
    for i in range(256):
        if i==0 :
            eq_hist1[i]=hist1[i]
            eq_hist2[i]=hist2[i]
        else:
            eq_hist1[i]=eq_hist1[i-1]+hist1[i]
            eq_hist2[i]=eq_hist2[i-1]+hist2[i]
            
    mapping=np.zeros(256)
    for i in range(256):
        for j in range(256):
            if(eq_hist1[i]<=eq_hist2[j]):
                mapping[i]=j+1
                break
        
        
    for i in range(len(img1)):
        for j in range(len(img1[0])):
            img1[i][j]=mapping[int(img1[i][j])]
            
    cv2.imshow('Modified original Image',img1)
    plt.hist(img1.flatten(),bins=256,label='Modified original Image Histogram',alpha=0.5)
    
    
Histogram_matching()
plt.legend()
plt.show()