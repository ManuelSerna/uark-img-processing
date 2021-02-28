# Threshold Demo
# Treshold code from OpenCV docs:
'''
https://docs.opencv.org/master/d7/d4d/tutorial_py_thresholding.html
'''

import cv2
import numpy as np
import matplotlib.pyplot as plt
import sys

img_name = sys.argv[1]
img = cv2.imread(img_name,0)

# Demo 1: global thresholding
'''
t = 150 # threshold intensity
mapping = 255 # map intensities >t to this intensity

ret,thresh1 = cv2.threshold(img,t_min,t_max,cv2.THRESH_BINARY)
ret,thresh2 = cv2.threshold(img,t_min,t_max,cv2.THRESH_BINARY_INV)
ret,thresh3 = cv2.threshold(img,t_min,t_max,cv2.THRESH_TRUNC)
ret,thresh4 = cv2.threshold(img,t_min,t_max,cv2.THRESH_TOZERO)
ret,thresh5 = cv2.threshold(img,t_min,t_max,cv2.THRESH_TOZERO_INV)

titles = ['Original Image','BINARY','BINARY_INV','TRUNC','TOZERO','TOZERO_INV']
images = [img, thresh1, thresh2, thresh3, thresh4, thresh5]

for i in range(6):
    plt.subplot(2,3,i+1),plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])

plt.show()
'''

# Demo 2: adaptive thresholding
# Adaptive thresholding can help in cases where lighting is not uniform across image

img = cv2.medianBlur(img,5)

ret,th1 = cv2.threshold(img,127,255,cv2.THRESH_BINARY)

th2 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY,11,2)

th3 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY,11,2)

titles = ['Original Image', 'Global Thresholding (v = 127)',
            'Adaptive Mean Thresholding', 'Adaptive Gaussian Thresholding']

images = [img, th1, th2, th3]

for i in range(4):
    plt.subplot(2,2,i+1),plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])
plt.show()
