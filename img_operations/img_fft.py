#*********************************
# Use Fast Fourier Transform on Image
'''
Call:

	$ python img_fft.py <img_name>

where:
	<img_name> is name of image file
'''
#*********************************

import cv2
import numpy as np
import matplotlib.pyplot as plt
import sys

img_name = sys.argv[1]
img = cv2.imread(img_name, 0) # take in grayscale image

# Use numpy's FFT package to perform frequency transform
f = np.fft.fft2(img)
fshift = np.fft.fftshift(f)
magnitude_spectrum = 20*np.log(np.abs(fshift))

# Plot image and magnitude spectrum
plt.subplot(121),plt.imshow(img, cmap = 'gray')
plt.title('Input Image'), plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(magnitude_spectrum, cmap = 'gray')
plt.title('Magnitude Spectrum'), plt.xticks([]), plt.yticks([])
plt.show()

