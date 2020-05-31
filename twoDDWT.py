from oneDDWT import *
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches

def twoDDWT(image_input,scale):
    image = np.copy(image_input)
    (l,c) = np.shape(image)

    for il in range(l):     #run through the lines
        image[il,:] = one_DDWT(image[il,:],scale)

    for ic in range(c):     #run through the columns
        image[:, ic] = one_DDWT(image[:, ic], scale)


    return image

def inverse_twoDDWT(image_input,scale):
    image = np.copy(image_input)
    (l,c) = np.shape(image)

    for ic in range(c):
        image[:,ic] = inverse_one_DDWT(image[:,ic],scale)

    for il in range(l):
        image[il,:] = inverse_one_DDWT(image[il,:],scale)

    return image

def plot_transform(transform, scale):
    (l,c) = np.shape(transform)

    ig, ax = plt.subplots(1)
    ax.imshow(transform,cmap='gray')

    for i in range(scale):
        rect = patches.Rectangle((l//2, c//2), l//2, c//2, linewidth=1, edgecolor='b', alpha = 0.1)
        ax.add_patch(rect)
        l = l//2
        c = c//2

    plt.show()