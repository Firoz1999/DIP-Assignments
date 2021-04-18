#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 18 20:54:43 2021

@author: firoz
"""

import numpy as np
import matplotlib.pyplot as plt
import cv2

Lena=cv2.imread('Lena.png')
Lena_gray =np.array(cv2.cvtColor(Lena, cv2.COLOR_BGR2GRAY))
i_r=len(Lena_gray)
i_c=len(Lena_gray[0])

eye=cv2.imread('left_eye.png')
eye_gray = np.array(cv2.cvtColor(eye, cv2.COLOR_BGR2GRAY))
t_r=len(eye_gray)
t_c=len(eye_gray[0])
    
zero_r=np.zeros((t_r//2,i_c))
Lena_gray=np.append(Lena_gray,zero_r,axis=0)
Lena_gray=np.concatenate((zero_r,Lena_gray),axis=0)
    
zero_c=np.zeros((i_r+2*(t_r//2),t_c//2))
Lena_gray=np.concatenate((zero_c,Lena_gray),axis=1)
Lena_gray=np.concatenate((Lena_gray,zero_c),axis=1)
    
result=np.zeros((i_r+t_r,i_c+t_c))
    
#print(np.std(eye_gray))
#print(np.mean(eye_gray))
eye_gray=(eye_gray-np.mean(eye_gray))/(np.std(eye_gray)*len(eye_gray))
count=0
for i in range(len(Lena_gray)-len(eye_gray)+1):
    for j in range(len(Lena_gray[0])-len(eye_gray[0])+1):
        s_r=i 
        e_r=i+len(eye_gray)
        s_c=j
        e_c=j+len(eye_gray[0])
        temp=Lena_gray[s_r:e_r,s_c:e_c]
        temp=(temp-np.mean(temp))/(np.std(temp)*len(temp))
        cor=np.sum(np.multiply(temp,eye_gray))
        result[i+int((len(eye_gray)-1)/2)][j+int((len(eye_gray[0])-1)/2)]=cor
    
maxx1=np.amax(result)
ind = np.where(result == np.amax(result))
ind=np.array(ind)
x1=ind[0][0]
y1=ind[1][0]
    
font = cv2.FONT_HERSHEY_SIMPLEX
color1=(255,255,255)
st1=(y1-t_c,x1-t_r)
en1=(y1,x1)
mid1=(y1-t_c/2,x1-t_r/2)
color=(0,0,255)
im1=cv2.rectangle(Lena,st1,en1,color,thickness=3)

cv2.imshow('Left eye location : ',im1)
