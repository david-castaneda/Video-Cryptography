from PIL import Image
from scipy import misc
import numpy as np
import os

# Function to encrypt an image
def encrypt(image):
    # Transforms image into a 1D array
    d = image.flatten()
    nx = len(image)
    ny = len(image[0])
    nz = len(image[0][0])
    count = 0
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
    encrypted_image.save('./dirty/ecnrypted_image_%d.JPG' %count)

# Path to clean images
path = './clean'

# Read all images from path
for cleanImage in os.listdir(path):
    i = misc.imread('./clean/%s' %cleanImage)
    encrypt(i)
