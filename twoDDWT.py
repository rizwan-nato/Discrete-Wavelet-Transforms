from oneDDWT import *
import numpy as np
import matplotlib.pyplot as plt
import cv2


def twoDDWT(image,scale):
    (l,c) = np.shape(image)
    for il in range(l):    #run through the lines
        image[il,:] = one_DDWT(image[il,:],scale)


    for ic in range(c):
        image[:,ic] = one_DDWT(image[:,ic],scale)
    return image

def inverse_twoDDWT(image,scale):
    (l,c) = np.shape(image)
    for ic in range(c):
        image[:,ic] = inverse_one_DDWT(image[:,ic],scale)


    for il in range(l):    #run through the lines
        image[il,:] = inverse_one_DDWT(image[il,:],scale)



    return image

image = cv2.imread('image.png', cv2.IMREAD_GRAYSCALE)
image = image.astype('float64')

scale = 2

transform = twoDDWT(image,scale)
plt.figure(1)
plt.imshow(transform,cmap='gray')
plt.show()

reconstruct = inverse_twoDDWT(transform,scale)
plt.figure(2)
plt.imshow(reconstruct,cmap='gray')
plt.show()