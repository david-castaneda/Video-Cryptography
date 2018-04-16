import numpy as np
import glob
import cv2
import os

# Decorator to allow other functions to be exectue after one another
def run_after(f_after):
    def wrapper(f):
        def wrapped(*args, **kwargs):
            ret = f(*args, **kwargs)
            f_after()
            return ret
        return wrapped
    return wrapper

# File Clean up
def cleaner():
    # Deletes Mac File from directory if it exists
    if(os.path.isfile('./clean/.DS_Store')):
        os.remove('./clean/.DS_Store')
    image_list = []
    for filename in glob.glob('./clean/*.jpg'):
        image_list.append(filename)
    image_list.sort()
    le = image_list[-1]
    os.remove('%s' %le)
    print('Clean up completed ✓')
    
@run_after(cleaner)
# Function to chunk video into frames
def framer(pathIn, pathOut):
    # Framer count
    count = 1
    # Read video using OpenCV
    vidcap = cv2.VideoCapture(pathIn)
    success,image = vidcap.read()
    success = True
    while success:
        # Sets image capture to 24 frames per second
      vidcap.set(cv2.CAP_PROP_POS_MSEC,(count*45))  
      success,image = vidcap.read()
      print ('Frame ', count, ' Processed.')
      cv2.imwrite( pathOut + "%07d_clean_image.jpg" % count, image)  
      count += 1
    
pathIn = './video.mp4'
pathOut = './clean/'
framer(pathIn, pathOut)
