import cv2
import numpy as np

THRESHOLD = 25
background = cv2.imread('vtest-f1.jpg')
background = cv2.cvtColor(background, cv2.COLOR_BGR2GRAY)
f1 = cv2.imread('vtest-f2.jpg')
f1 = cv2.cvtColor(f1, cv2.COLOR_BGR2GRAY)
result = np.zeros(shape=background.shape)
result_thresholded = np.zeros(shape=background.shape)

for y in range(background.shape[0]):
    for x in range(background.shape[1]):
        # pada cv2.imread tipe ruang warna yang digunakan adalah BGR
    # Jika menggunakan RGB
        # red = abs(int(f1[y][x][2])-int(background[y][x][2]))
        # blue = abs(int(f1[y][x][1])-int(background[y][x][1]))
        # green = abs(int(f1[y][x][0])-int(background[y][x][0]))
        # color = [
        #     255 if blue>THRESHOLD else 0, 
        #     255 if green>THRESHOLD else 0, 
        #     255 if red>THRESHOLD else 0
        #     ]
    # Jika menggunakan Grayscale
        color_thresholded = 255 if abs(int(background[y][x])-int(f1[y][x]))>25 else 0
        color = abs(int(background[y][x])-int(f1[y][x]))
        result[y][x] = color
        result_thresholded[y][x] = color_thresholded

result_thresholded = cv2.dilate(result_thresholded, np.ones((3,3), np.uint8),iterations=1)
result_thresholded = cv2.erode(result_thresholded, np.ones((2,2), np.uint8),iterations=3)
result_thresholded = cv2.dilate(result_thresholded, np.ones((3,3), np.uint8),iterations=5)
cv2.imwrite('vtest-result.jpg', result_thresholded)
cv2.imshow('Result', result)
cv2.imshow('Thresholded', result_thresholded)
cv2.waitKey(0)