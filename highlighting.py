import cv2

img = cv2.imread('vtest-result.jpg')
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
print(img[img==255])
x_list = []
y_list = []
for y in range(img.shape[0]):
    for x in range(img.shape[1]):
        if img[y][x]==255:
            print('found: ',x)
            x_list.append(x)
            y_list.append(y)

x_min = min(x_list)
x_max = max(x_list)
y_min = min(y_list)
y_max = max(y_list)
print('X: (',x_min,',',x_max,')')
print('Y: (',y_min,',',y_max,')')

result = cv2.imread('vtest-f1.jpg')
# Draw rectangle
result[y_min, x_min:x_max] = [0,255,0]
result[y_max, x_min:x_max] = [0,255,0]
result[y_min:y_max, x_min] = [0,255,0]
result[y_min:y_max, x_max] = [0,255,0]

cv2.imshow('Grayscale', img)
cv2.imshow('Result', result)
cv2.waitKey(0)