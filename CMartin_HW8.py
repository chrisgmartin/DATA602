#This homework will give you a chance to explore some image processing techniques in Python.
#These are some of the most basic tasks done in image processing.

#First, download the image package attached to this lesson.
#On each image you will count the number of objects in the image and find their center points. 
#The images in order of complexity are circles.png, objects.png and peppers.png.

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from scipy import misc
import scipy.ndimage as ndimage
import skimage.filter as skif
from skimage import color
from skimage import io
from pylab import *
import mahotas as mh

circles_url = 'C:/Users/itsal/Documents/CUNY/DATA602/circles.png'
objects_url = 'C:/Users/itsal/Documents/CUNY/DATA602/objects.png'
peppers_url = 'C:/Users/itsal/Documents/CUNY/DATA602/peppers.png'



#Using Python's built-in functionality, scipy, or any other module, perform the following tasks:

#Thresholding:
#First convert the image to a binary image.
#This is done with a technique called thresholding, which is covered in the reading.
#There are functions for it in scipy, although it is very easy to do manually.
#Essentially read each pixel and if it above a specified gray level make it white, otherwise make it black.


#global threshold technique
def global_technique(image_url):
    newimg = misc.imread(image_url, mode='L')
    global_thresh = skif.threshold_otsu(newimg)
    global_cut = newimg > global_thresh
    return imshow(global_cut)

global_technique(circles_url)
global_technique(objects_url)
global_technique(peppers_url)


#Count objects:
#Count the number of objects in the image.
#If you are interested in how this is done, refer to the additional readings.
#An object will be a group of white pixels surrounded by black pixels.
#Doing this by hand is also fairly easy, but try to use functions found in the modules available.

def counter(image_url):
    newimg = misc.imread(image_url, mode='L')
    global_thresh = skif.threshold_otsu(newimg)
    labeled, nr_objects = mh.label(newimg > global_thresh)
    return nr_objects

counter(circles_url)
counter(objects_url)
counter(peppers_url)

#just out of curiosity
#how does the counter work with a gaussian filter
def clean_counter(image_url):
    newimg = misc.imread(image_url, mode='L')
    glimg = mh.gaussian_filter(newimg, 8)
    global_thresh = skif.threshold_otsu(newimg)
    labeled, nr_objects = mh.label(newimg > global_thresh)
    return nr_objects

clean_counter(circles_url)
clean_counter(objects_url)
clean_counter(peppers_url)

#Find center points:
#For each object, find the center point in terms of x,y coordinates.
#As with part 3, you can do this directly, but it's better to use something from a module.
#Image files can be read in directly or you can use a dialog box.
#Your output will list the objects and midpoints for each image.
#Remember, the focus here is to use readily available Python functions to do image processing rather
#than gain a deep understanding of the theory of the techniques.
#For the peppers.png image, I’m not expecting a specific number, as the answer is fairly subjective.
#The focus is on the process, not the result.


def center(image_url):
    newimg = misc.imread(image_url, mode='L')
    lbl = ndimage.label(newimg)[0]
    return ndimage.measurements.center_of_mass(newimg, lbl)

center(circles_url)
center(objects_url)
center(peppers_url)