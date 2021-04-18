#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 18 16:47:12 2021

@author: firoz
"""

import numpy as np
import matplotlib.pyplot as plt
import cv2

cropped_img=['0.png','1.png','2.png','3.png','4.png','5.png','6.png','7.png','9.png']
im1=[]
fig,ax=plt.subplots(3,3,figsize=(9,9))
for l in range(9):
    image=cv2.imread('hdraw.png')
    image_gray =np.array(cv2.cvtColor(image, cv2.COLOR_BGR2GRAY))
    i_r=len(image_gray)
    i_c=len(image_gray[0])
    
    crop_img=cv2.imread(cropped_img[l])
    crop_img_gray = np.array(cv2.cvtColor(crop_img, cv2.COLOR_BGR2GRAY))
    t_r=len(crop_img_gray)
    t_c=len(crop_img_gray[0])
    
    zero_r=np.zeros((t_r//2,i_c))
    image_gray=np.append(image_gray,zero_r,axis=0)
    image_gray=np.concatenate((zero_r,image_gray),axis=0)
    
    zero_c=np.zeros((i_r+2*(t_r//2),t_c//2))
    image_gray=np.concatenate((zero_c,image_gray),axis=1)
    image_gray=np.concatenate((image_gray,zero_c),axis=1)
    
    result=np.zeros((i_r+t_r,i_c+t_c))
    
    count=0
    for i in range(len(image_gray)-len(crop_img_gray)+1):
        for j in range(len(image_gray[0])-len(crop_img_gray[0])+1):
            s_r=i 
            e_r=i+len(crop_img_gray)
            s_c=j
            e_c=j+len(crop_img_gray[0])
            temp=image_gray[s_r:e_r,s_c:e_c]
            cor=np.sum(np.multiply(temp,crop_img_gray))
            result[i+int((len(crop_img_gray)-1)/2)][j+int((len(crop_img_gray[0])-1)/2)]=cor
    
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
    im1.append(cv2.rectangle(image,st1,en1,color,thickness=5))

ax[0,0].imshow(im1[0])
ax[0,1].imshow(im1[1])
ax[0,2].imshow(im1[2])
ax[1,0].imshow(im1[3])
ax[1,1].imshow(im1[4])
ax[1,2].imshow(im1[5])
ax[2,0].imshow(im1[6])
ax[2,1].imshow(im1[7])
ax[2,2].imshow(im1[8])