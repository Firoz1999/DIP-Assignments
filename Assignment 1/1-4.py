#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 21 16:29:36 2021

@author: vaibhav
"""

import numpy as np
import cv2
import math
import matplotlib.pyplot as plt

def bilinear_resize(image, height, width):
  img_height, img_width = image.shape[:2]

  resized = np.empty([height, width])

  x_ratio = float(img_width - 1) / (width - 1)
  y_ratio = float(img_height - 1) / (height - 1)

  for i in range(height):
    for j in range(width):

      x_l, y_l = math.floor(x_ratio * j), math.floor(y_ratio * i)
      x_h, y_h = math.ceil(x_ratio * j), math.ceil(y_ratio * i)

      x_weight = (x_ratio * j) - x_l
      y_weight = (y_ratio * i) - y_l

      a = image[y_l, x_l]
      b = image[y_l, x_h]
      c = image[y_h, x_l]
      d = image[y_h, x_h]

      pixel = a * (1 - x_weight) * (1 - y_weight) + b * x_weight * (1 - y_weight) + c * y_weight * (1 - x_weight) + d * x_weight * y_weight

      resized[i][j] = pixel

  return resized

def mse(imageA, imageB):
	err = np.sum((imageA.astype("float") - imageB.astype("float")) ** 2)
	err /= float(imageA.shape[0] * imageA.shape[1] * 3)
	return err

def bilinear_color(image,scale):
  h,w,_=image.shape
  b,g,r = cv2.split(image)
  new_h=int(h*scale)
  new_w=int(w*scale)
  b1=bilinear_resize(b,new_h,new_w).astype('uint8')
  g1=bilinear_resize(g,new_h,new_w).astype('uint8')
  r1=bilinear_resize(r,new_h,new_w).astype('uint8')
  final = cv2.merge((b1,g1,r1))
  return final


image=cv2.imread('lena.jpg')

cv2.imshow("Input Image",image)
i1=bilinear_color(image,0.5)
cv2.imshow("Scale: 0.5 Own Func",i1)
i2=cv2.resize(image, None, fx = 0.5, fy = 0.5)
cv2.imshow("Scale: 0.5 In Built Func",i2)
i3=bilinear_color(image,2)
cv2.imshow("Scale: 2 Own Func",i3)
i4=cv2.resize(image, None, fx = 2, fy = 2)
cv2.imshow("Scale: 2 In Built Func",i4)

print("Mean Square Error for scale 0.5",mse(i1,i2))
print("Mean Square Error for scale 2",mse(i3,i4))


