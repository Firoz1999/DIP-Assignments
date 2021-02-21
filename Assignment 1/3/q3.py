import cv2
from matplotlib import pyplot as plt
from skimage.util import random_noise
img_original=cv2.imread("./lena.jpg")# reading in Grey Scale
img_original= cv2.cvtColor(img_original, cv2.COLOR_BGR2RGB) # converting RBG to RGB value
img_gray= cv2.cvtColor(img_original,cv2.COLOR_BGR2GRAY) # converting RBG to Grey value
plt.subplot(1,2,1)
plt.title("Original")
plt.axis("off")
plt.imshow(img_original)
plt.subplot(1,2,2)
plt.title("Grayscale")
plt.axis("off")
plt.imshow(img_gray,cmap='gray')
plt.show()

def salt_pepper(img):
    spnoise = []
    for j in range(6):
        spnoise.append(random_noise(img, mode='s&p',amount=0.01))
        for i in range((j+1)*5-1):
            spnoise[j] =random_noise(spnoise[j], mode='s&p',amount=0.01)
    plt.suptitle("Salt and Pepper Noise")
    for i in range(6):
        plt.subplot(2,3,i+1)
        plt.imshow(spnoise[i],cmap='gray')
        plt.axis("off")
        plt.title(str((i+1)*5)+" times")
    plt.show()

def gauss(img):
    gausNoise =[]
    for i in range(6):
        gausNoise.append(random_noise(img, mode='gaussian',mean=0,var=0.01))
        for j in range((i+1)*(5)-1):
            gausNoise[i] = random_noise(gausNoise[i], mode='gaussian',mean=0,var=0.01)
    plt.suptitle("Gaussian Noise")
    for i in range(6):
        plt.subplot(2,3,i+1)
        plt.imshow(gausNoise[i],cmap='gray')
        plt.axis('off')
        plt.title(str((i+1)*5)+" times")
    plt.imshow(gausNoise[5],cmap='gray')
    plt.show()

def speckle(img):
    speckleNoise =[]
    for i in range(6):
        speckleNoise.append(random_noise(img,mode='speckle',mean=0,var=0.01))
        for j in range((i+1)*5-1):
            speckleNoise[i]=(random_noise(speckleNoise[i],mode='speckle',mean=0,var=0.01))
    for i in range(6):
        plt.subplot(2,3,i+1)
        plt.imshow(speckleNoise[i],cmap='gray')
        plt.axis('off')
        plt.title(str((i+1)*5)+" times")
    plt.suptitle("Speckle Noise")
    plt.show()

salt_pepper(img_gray)
gauss(img_gray)
speckle(img_gray)
