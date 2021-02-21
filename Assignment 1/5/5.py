#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 21 21:09:33 2021

@author: vaibhav
"""

import cv2
import numpy as np
import matplotlib.pyplot as plt
import imutils

def rotateImage(Image, angle):
    rotatedImage = imutils.rotate(Image, angle)
    return rotatedImage

image = 'tower.jpeg'
I = cv2.imread(image, 0)
I = cv2.cvtColor(I, cv2.COLOR_BGR2RGB)

fig, ax = plt.subplots(1, 5,figsize=(15,15))
ax[0].imshow(I)
ax[0].set_title("Input Image")

angles = list(np.arange(2, 6, 1))

for i in range(4):
  ax[i+1].set_title("Angle: "+str(angles[i]))
  ax[i+1].imshow(rotateImage(I, angles[i]))
print("The angle of inclination of leaning tower of pisa is approx. 4 Degrees")
