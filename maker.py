import os
import glob
from PIL import Image
from cv2 import VideoWriter, VideoWriter_fourcc, imread, resize

def maker(images, outimg=None, fps=24, size=None, is_color=True, format="mp4v"):
    fourcc = VideoWriter_fourcc(*format)
    vid = None
    outvid = './dirty_video.mp4'
    for image in images:
        if not os.path.exists(image):
            raise FileNotFoundError(image)
        img = imread(image)
        if vid is None:
            if size is None:
                size = img.shape[1], img.shape[0]
            vid = VideoWriter(outvid, fourcc, float(fps), size, is_color)
        if size[0] != img.shape[1] and size[1] != img.shape[0]:
            img = resize(img, size)
        vid.write(img)
    vid.release()
    return vid

image_list = []
for filename in glob.glob('dirty/*.jpg'):
    image_list.append(filename)

image_list.sort()
maker(image_list)