#*********************************
# Get image histogram
'''
Call:

	$ python histogram.py <img_name>

where:
	<img_name> is the file name of the input image
'''
#*********************************

import cv2
import numpy as np
import matplotlib.pyplot as plt
import sys

'''
Histograms give a distribution of the pixel intensity values.
By using image histograms, we can get a better idea about the contrast,
brightness, intensity dist., etc.

Use 'bins' to count number of pixles that fall within a certain intensity range.
(e.g. 256 bins for all 256 intensity values, or 16 bins, or 32, etc.)
'''

img_name = sys.argv[1]
print('Image {}'.format(img_name))

#img = cv2.imread(img_name, 0) # get image

# Using opencv to calculate histogram
#hist = cv2.calcHist([img], [0], None, [256], [0, 256])

# Using numpy to calculate histogram (grayscale), and display it
#plt.hist(img.ravel(), 256, [0, 256])
#plt.show()

# Using cv2 to calculate color histograms
img = cv2.imread(img_name)
color = ('b','g','r')

for i,col in enumerate(color):
    histr = cv2.calcHist([img],[i],None,[256],[0,256])
    plt.plot(histr,color = col)
    plt.xlim([0,256])

plt.show()

