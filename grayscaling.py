# Reference: https://www.dynamsoft.com/blog/insights/image-processing/image-processing-101-color-space-conversion/

import cv2
import numpy as np

img = cv2.imread('vtest-f1.jpg')
result = np.zeros(shape=img.shape[:-1])
# cv2.imshow('Original', img)
# cv2.waitKey(0)


# Rumus untuk grayscale menggunakan NTSC Format
    # Red * 0.299
    # Green * 0.587
    # Blue * 0.114
# Cara lain adalah dengan menghitung nilai rata-rata dari r, g, dan b
    # Red/3
    # Green/3
    # Blue/3
for y in range(img.shape[0]):
    for x in range(img.shape[1]):
    # Jika menggunakan NTSC Format
        # red = img[y][x][2] * 0.299
        # green = img[y][x][1] * 0.587
        # blue = img[y][x][0] * 0.114
        # color = blue+green+red
    # Jika menggunakan rata-rata
        red = img[y][x][2]/3
        green = img[y][x][1]/3
        blue = img[y][x][0]/3
        color = blue+green+red
        print('y: ', y, ' x: ',x,' : ',color)
        result[y][x] = color
        
cv2.imshow('Grayscale',result)
cv2.waitKey(0)
