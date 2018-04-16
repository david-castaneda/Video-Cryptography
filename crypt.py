from PIL import Image
from scipy import misc
import numpy as np
import time
import os
import glob


#Image counter
count = 0

# Function to encrypt an image
def encrypt(image):
    global count
    # Transforms image into a 1D array
    d = image.flatten()
    nx = len(image)
    ny = len(image[0])
    nz = len(image[0][0])
    # Iterate through the 1D array and 
    # encrypt each value
    for i in range(0, image.size):
        # Test mod encryption
        d[i] = d[i] % 100
    # Counter for images that have been processed
    count += 1
    # Reshaped 1D image into a matrix
    encrypted_image_3d = d.reshape((nx,ny,nz))

    # Converts matrix back into an image, then saves the images
    encrypted_image = Image.fromarray(encrypted_image_3d, 'RGB')    
    encrypted_image.save('./dirty/%07d_encrypted_image.jpg' %count)
    print('Frame %d Encrypted' %count)

# Path to clean images
path = './clean'

image_list = []
for filename in glob.glob('clean/*.jpg'):
    image_list.append(filename)
image_list.sort()

# Read all images from image_list and encrypts them
for image in image_list:
    img = misc.imread(image)    
    encrypt(img)
