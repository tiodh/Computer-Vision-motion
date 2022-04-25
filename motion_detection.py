import cv2
import numpy as np
from sklearn.cluster import DBSCAN


THRESHOLD = 25

cap = cv2.VideoCapture("vtest.mp4")
ret, f1 = cap.read()
cv2.imshow("Video", f1)
cv2.waitKey(0)
while cap.isOpened():
    ret, f2 = cap.read()

    f1_gray = cv2.cvtColor(f1,cv2.COLOR_BGR2GRAY)
    f2_gray = cv2.cvtColor(f2,cv2.COLOR_BGR2GRAY)
    subtract = f1_gray-f2_gray
    subtract[subtract>THRESHOLD] = 255
    subtract[subtract<=THRESHOLD] = 0

    subtract = cv2.erode(subtract, np.ones((2,2), np.uint8),iterations=2)
    subtract = cv2.dilate(subtract, np.ones((2,2), np.uint8),iterations=2)

    obj = []
    for y in range(subtract.shape[0]):
        for x in range(1,subtract.shape[1]-1):
            if subtract[y][x]==255:
                obj.append([y,x])

    obj = np.array(obj)
    clustering = DBSCAN(eps=3, min_samples=5).fit(obj)
    labels = clustering.labels_

    obj_label = np.zeros((obj.shape[0], obj.shape[1]+1), int)
    obj_label[:,:2] = obj
    obj_label[:,2] = labels
    
    for i in np.unique(labels):
        if len(obj_label[obj_label[:,2]==i])<300:
            obj_label = obj_label[obj_label[:,2]!=i]
    labels = np.unique(obj_label[:,2])
    print(labels)

    for i in labels:
        sliced = obj_label[(obj_label[:,2]==i)]
        min_y = np.amin(sliced[:,0])
        max_y = np.amax(sliced[:,0])
        min_x = np.amin(sliced[:,1])
        max_x = np.amax(sliced[:,1])
        
        # Draw Rectangle
        f2[min_y, min_x:max_x] = [0,255,0]
        f2[max_y, min_x:max_x] = [0,255,0]
        f2[min_y:max_y, min_x] = [0,255,0]
        f2[min_y:max_y, max_x] = [0,255,0]

    cv2.imshow("Video", f2)
    cv2.imshow("Threshold", subtract)
    cv2.waitKey(1)
    f1 = f2
    


# background = cv2.imread('vtest-f1.jpg')
# background = cv2.cvtColor(background, cv2.COLOR_BGR2GRAY)
# f1 = cv2.imread('vtest-f2.jpg')
# f1 = cv2.cvtColor(f1, cv2.COLOR_BGR2GRAY)
# result = np.zeros(shape=background.shape)
# result_thresholded = np.zeros(shape=background.shape)

# for y in range(background.shape[0]):
#     for x in range(background.shape[1]):
#         color_thresholded = 255 if abs(int(background[y][x])-int(f1[y][x]))>25 else 0
#         color = abs(int(background[y][x])-int(f1[y][x]))
#         result[y][x] = color
#         result_thresholded[y][x] = color_thresholded




# obj = []
# for y in range(result_thresholded.shape[0]):
#     for x in range(1,result_thresholded.shape[1]-1):
#         if result_thresholded[y][x]==255:
#             obj.append([y,x])

# obj = np.array(obj)
# clustering = DBSCAN(eps=3, min_samples=2).fit(obj)
# labels = clustering.labels_

# obj_label = np.zeros((obj.shape[0], obj.shape[1]+1), int)
# obj_label[:,:2] = obj
# obj_label[:,2] = labels


# for i in labels:
#     sliced = obj_label[(obj_label[:,2]==i)]
#     min_y = np.amin(sliced[:,0])
#     max_y = np.amax(sliced[:,0])
#     min_x = np.amin(sliced[:,1])
#     max_x = np.amax(sliced[:,1])
    
#     # Draw Rectangle
#     result[min_y, min_x:max_x] = [0,255,0]
#     result[max_y, min_x:max_x] = [0,255,0]
#     result[min_y:max_y, min_x] = [0,255,0]
#     result[min_y:max_y, max_x] = [0,255,0]
# cv2.imshow('Thresholded', img)
# cv2.imshow('Localization', result)
# cv2.waitKey(0)