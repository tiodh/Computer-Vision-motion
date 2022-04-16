from turtle import shape

from sklearn import cluster
import cv2
import numpy as np
from sklearn.cluster import DBSCAN

f1 = cv2.imread('vtest-f1.jpg')
f2 = cv2.imread('vtest-f2.jpg')
img = cv2.imread('vtest-result.jpg')
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
result = cv2.imread('vtest-f2.jpg')

obj = []
for y in range(img.shape[0]):
    for x in range(1,img.shape[1]-1):
        if img[y][x]==255:
            obj.append([y,x])

obj = np.array(obj)
clustering = DBSCAN(eps=3, min_samples=2).fit(obj)
labels = clustering.labels_

obj_label = np.zeros((obj.shape[0], obj.shape[1]+1), int)
obj_label[:,:2] = obj
obj_label[:,2] = labels


for i in labels:
    sliced = obj_label[(obj_label[:,2]==i)]
    min_y = np.amin(sliced[:,0])
    max_y = np.amax(sliced[:,0])
    min_x = np.amin(sliced[:,1])
    max_x = np.amax(sliced[:,1])
    
    # Draw Rectangle
    result[min_y, min_x:max_x] = [0,255,0]
    result[max_y, min_x:max_x] = [0,255,0]
    result[min_y:max_y, min_x] = [0,255,0]
    result[min_y:max_y, max_x] = [0,255,0]

cv2.imshow('Thresholded', img)
cv2.imshow('Localization', result)
cv2.waitKey(0)