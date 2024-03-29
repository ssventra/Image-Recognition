# -*- coding: utf-8 -*-
"""Symbiosis_opencv_op.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ULy99dTZbsElhro7bGSpYB-j67S80Cpx

## Histograms are a great way to visualize individual color components

Importing Libraries
"""

import cv2
import numpy as np
# We need to import matplotlib to create our histogram plots
from matplotlib import pyplot as plt
from google.colab.patches import cv2_imshow

image = cv2.imread('/content/drive/MyDrive/Copy of input.jpg')

histogram = cv2.calcHist([image], [0], None, [256], [0, 256]) #for 256 pixels

# We plot a histogram, ravel() flatens our image array 
plt.hist(image.ravel(), 256, [0, 256]); plt.show()

# Viewing Separate Color Channels
color = ('b', 'g', 'r')

# We now separate the colors and plot each in the Histogram
for i, col in enumerate(color):
    histogram2 = cv2.calcHist([image], [i], None, [256], [0, 256]) #i channel
    plt.plot(histogram2, color = col)
    plt.xlim([0,256])
    
plt.show()

# more components from 0-50 hence more a dark image

image = cv2.imread('/content/drive/MyDrive/Copy of taj.jpg')

histogram = cv2.calcHist([image], [0], None, [256], [0, 256])

# We plot a histogram, ravel() flatens our image array 
plt.hist(image.ravel(), 256, [0, 256]); plt.show()

# Viewing Separate Color Channels
color = ('b', 'g', 'r')

# We now separate the colors and plot each in the Histogram
for i, col in enumerate(color):
    histogram2 = cv2.calcHist([image], [i], None, [256], [0, 256])
    plt.plot(histogram2, color = col)
    plt.xlim([0,256])
    
plt.show()
# Equally distributed histogram

"""**cv2.calcHist(images, channels, mask, histSize, ranges[, hist[, accumulate]])**

- images : it is the source image of type uint8 or float32. it should be given in square brackets, ie, "[img]".
- channels : it is also given in square brackets. It is the index of channel for which we calculate histogram. For example, if input is grayscale image, its value is [0]. For color image, you can pass [0], [1] or [2] to calculate histogram of blue, green or red channel respectively.
- mask : mask image. To find histogram of full image, it is given as "None". But if you want to find histogram of particular region of image, you have to create a mask image for that and give it as mask. (I will show an example later.)
- histSize : this represents our BIN count. Need to be given in square brackets. For full scale, we pass [256].
- ranges : this is our RANGE. Normally, it is [0,256].

## Histogram Equalization
"""

hist,bins=np.histogram(image.flatten(),256,[0,256])
plt.plot(hist,color='b')

cdf= hist.cumsum() # total cummulative

cdf_normalized= cdf*hist.max()/cdf.max()

plt.plot(cdf_normalized, color='b')

#  Source should be grey level channel
image = cv2.imread('/content/drive/MyDrive/Copy of input.jpg',0)
equ=cv2.equalizeHist(image)

hist,bins=np.histogram(equ.flatten(),256,[0,256])
plt.plot(hist,color='b')

"""## Task 2 

Load a new image and perform histogram equalization
"""

Picture = cv2.imread('/content/drive/MyDrive/Copy of elephant.jpg')

histogram4 = cv2.calcHist([Picture], [0], None, [256], [0, 256]) #for 256 pixels

# We plot a histogram, ravel() flatens our image array 
plt.hist(Picture.ravel(), 256, [0, 256]); plt.show()

# Viewing Separate Color Channels
color = ('b', 'g', 'r')

# We now separate the colors and plot each in the Histogram
for i, col in enumerate(color):
    histogram3 = cv2.calcHist([Picture], [i], None, [256], [0, 256]) #i channel
    plt.plot(histogram3, color = col)
    plt.xlim([0,256])
    
plt.show()

picture = cv2.imread('/content/drive/MyDrive/Copy of input.jpg',0)
equ=cv2.equalizeHist(image)

hist,bins=np.histogram(equal.flatten(),256,[0,256])
plt.plot(hist,color='b')

"""## Convolution operations - Blurring and Sharpning of the image """

image=cv2.imread('/content/drive/MyDrive/Copy of taj.jpg')
image=cv2.resize(image,(600,600))
kernel=np.ones((5,5),np.float32)/25 
# 5 rows and 5 columns diving it by 25 because sum of the values should always be 1.

conv=cv2.filter2D(image,-1,kernel)
cv2_imshow(conv)

cv2_imshow(image)
cv2.waitKey(0)
cv2.destroyAllWindows()

"""## Task 3
load the image(new image of your choice ) and convolve it with different kernel size[(3,3),(7,7),(9,9)] 
"""

kernel=np.ones((3,3),np.float32)/9
# 5 rows and 5 columns diving it by 25 because sum of the values should always be 1.

conv=cv2.filter2D(image,-1,kernel)
cv2_imshow(conv)

kernel=np.ones((7,7),np.float32)/49
# 5 rows and 5 columns diving it by 25 because sum of the values should always be 1.

conv=cv2.filter2D(image,-1,kernel)
cv2_imshow(conv)

kernel=np.ones((9,9),np.float32)/81 
# 5 rows and 5 columns diving it by 25 because sum of the values should always be 1.

conv=cv2.filter2D(image,-1,kernel)
cv2_imshow(conv)

"""## commonly used blurring methods in OpenCV"""

image = cv2.imread('/content/drive/MyDrive/Copy of elephant.jpg')

# Averaging done by convolving the image with a normalized box filter. 
# This takes the pixels under the box and replaces the central element
# Box size needs to odd and positive 
blur = cv2.blur(image, (3,3))
cv2_imshow(blur)
cv2.waitKey(0)

# Instead of box filter, gaussian kernel
Gaussian = cv2.GaussianBlur(image, (7,7), 0)
cv2_imshow(Gaussian)
cv2.waitKey(0)

# Takes median of all the pixels under kernel area and central 
# element is replaced with this median value
median = cv2.medianBlur(image, 5)
cv2_imshow(median)
cv2.waitKey(0)

# Bilateral is very effective in noise removal while keeping edges sharp
bilateral = cv2.bilateralFilter(image, 9, 75, 75)
cv2_imshow(bilateral)
cv2.waitKey(0)
cv2.destroyAllWindows()

"""## Task 4 

use different blur function for images
"""



image = cv2.imread('/content/drive/MyDrive/Copy of input.jpg')
cv2_imshow(image)

# Create our shapening kernel, we don't normalize since the 
# the values in the matrix sum to 1
kernel_sharpening = np.array([[-1,-1,-1], 
                              [-1,9,-1], 
                              [-1,-1,-1]])

# applying different kernels to the input image
sharpened = cv2.filter2D(image, -1, kernel_sharpening)

cv2_imshow(sharpened)

cv2.waitKey(0)
cv2.destroyAllWindows()

"""## Thresholding """

# Load our image as greyscale 
image = cv2.imread('/content/drive/MyDrive/Copy of input.jpg',0)
cv2_imshow(image)

# Values below 127 goes to 0 (black, everything above goes to 255 (white)
ret,thresh1 = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY)
cv2_imshow(thresh1)

# Values below 127 go to 255 and values above 127 go to 0 (reverse of above)
ret,thresh2 = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY_INV)
cv2_imshow(thresh2)

# Values above 127 are truncated (held) at 127 (the 255 argument is unused)
ret,thresh3 = cv2.threshold(image, 127, 255, cv2.THRESH_TRUNC)
cv2_imshow(thresh3)

# Values below 127 go to 0, above 127 are unchanged  
ret,thresh4 = cv2.threshold(image, 127, 255, cv2.THRESH_TOZERO)
cv2_imshow(thresh4)

# Resever of above, below 127 is unchanged, above 127 goes to 0
ret,thresh5 = cv2.threshold(image, 127, 255, cv2.THRESH_TOZERO_INV)
cv2_imshow(thresh5)
cv2.waitKey(0) 
    
cv2.destroyAllWindows()

"""## Adaptive thresholding """

# Load our new image
image = cv2.imread('/content/drive/MyDrive/Copy of Origin_of_Species.jpg', 0)

cv2_imshow(image)
cv2.waitKey(0)

# Values below 127 goes to 0 (black, everything above goes to 255 (white)
ret,thresh1 = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY)
cv2_imshow(thresh1)
cv2.waitKey(0)

# It's good practice to blur images as it removes noise
image = cv2.GaussianBlur(image, (3, 3), 0)

# Using adaptiveThreshold
thresh = cv2.adaptiveThreshold(image, 255, cv2.ADAPTIVE_THRESH_MEAN_C, 
                               cv2.THRESH_BINARY, 3, 5) 
cv2_imshow(thresh) 
cv2.waitKey(0)

# It's good practice to blur images as it removes noise
image = cv2.GaussianBlur(image, (3, 3), 0)

# Using adaptiveThreshold
thresh = cv2.adaptiveThreshold(image, 255, cv2.ADAPTIVE_THRESH_MEAN_C, 
                               cv2.THRESH_BINARY, 3, 5) 
cv2_imshow(thresh) 
cv2.waitKey(0)

_, th2 = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
cv2_imshow(thresh) 
cv2.waitKey(0)

# Otsu's thresholding after Gaussian filtering
blur = cv2.GaussianBlur(image, (5,5), 0)
_, th3 = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
cv2_imshow(thresh) 
cv2.waitKey(0) 

cv2.destroyAllWindows()

"""## Dilation, Erosion, Opening and Closing"""

image = cv2.imread('/content/drive/MyDrive/Copy of opencv_inv.png', 0)
cv2_imshow(image)
cv2.waitKey(0)

# Let's define our kernel size
kernel = np.ones((5,5), np.uint8)

# Now we erode
erosion = cv2.erode(image, kernel, iterations = 1)
cv2_imshow(erosion)
cv2.waitKey(0)

dilation = cv2.dilate(image, kernel, iterations = 1)
cv2_imshow(dilation)
cv2.waitKey(0)

# Opening - Good for removing noise
opening = cv2.morphologyEx(image, cv2.MORPH_OPEN, kernel)
cv2_imshow(opening)
cv2.waitKey(0)

# Closing - Good for removing noise
closing = cv2.morphologyEx(image, cv2.MORPH_CLOSE, kernel)
cv2_imshow(closing)
cv2.waitKey(0)

"""## Edge detetion """

image = cv2.imread('/content/drive/MyDrive/Copy of input.jpg',0)

height, width = image.shape

# Extract Sobel Edges
sobel_x = cv2.Sobel(image, cv2.CV_64F, 0, 1, ksize=5)
sobel_y = cv2.Sobel(image, cv2.CV_64F, 1, 0, ksize=5)

cv2_imshow(image)
cv2.waitKey(0)

cv2_imshow(sobel_x)
cv2.waitKey(0)

cv2_imshow(sobel_y)
cv2.waitKey(0)

sobel_OR = cv2.bitwise_or(sobel_x, sobel_y)
cv2_imshow(sobel_OR)
cv2.waitKey(0)
cv2.destroyAllWindows()

#Laplacian

laplacian = cv2.Laplacian(image, cv2.CV_64F)
cv2_imshow(laplacian)
cv2.waitKey(0)
cv2.destroyAllWindows()

# #we need to provide two values: threshold1 and threshold2. Any gradient value larger than threshold2
# is considered to be an edge. Any value below threshold1 is considered not to be an edge. 
#Values in between threshold1 and threshold2 are either classiﬁed as edges or non-edges based on how their 
#intensities are “connected”. In this case, any gradient values below 50 are considered non-edges
#whereas any values above 120 are considered edges.


# Canny Edge Detection uses gradient values as thresholds
# The first threshold gradient
canny = cv2.Canny(image, 50, 120)
cv2_imshow(canny)
cv2.waitKey(0)

cv2.destroyAllWindows()

"""## Task Try to increases the intensity of threshold values """

