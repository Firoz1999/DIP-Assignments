#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 18 16:32:12 2021

@author: vaibhav
"""

import cv2
import numpy as np
from q2_4 import dft_2D
import matplotlib.pyplot as plt


def dft2_phase_mag():
  image = './images/Lena.png'
  image1 = './images/dog.png'
  I = cv2.imread(image)
  I = cv2.cvtColor(I, cv2.COLOR_BGR2GRAY)
  I1 = cv2.imread(image1)
  I1 = cv2.cvtColor(I1, cv2.COLOR_RGB2GRAY)
  
  lena_dft=dft_2D(I)
  dog_dft=dft_2D(I1)
  lena_mag = np.absolute(lena_dft)   
  lena_phase = np.angle(lena_dft)   
  dog_mag = np.absolute(dog_dft)
  dog_phase = np.angle(dog_dft)
  return lena_mag,lena_phase,dog_mag,dog_phase
  
if __name__ == "__main__":
  lena_mag,lena_phase,dog_mag,dog_phase=dft2_phase_mag()
  plt.subplot(2,2,1).set_title('Phase of Lena 2D DFT Image')
  plt.imshow(lena_phase, 'gray')
  plt.subplot(2,2,2).set_title('Magnitude of Lena 2D DFT Image')
  plt.imshow(20*np.log(lena_mag), 'gray') #for plotting purposes the mag has been reduced to logarithmic scale
  plt.subplot(2,2,3).set_title('Phase of Dog 2D DFT Image')
  plt.imshow(dog_phase, 'gray')
  plt.subplot(2,2,4).set_title('Magnitude of Dog 2D DFT Image')
  plt.imshow(20*np.log(dog_mag), 'gray') #for plotting purposes the mag has been reduced to logarithmic scale
  plt.show()
  
