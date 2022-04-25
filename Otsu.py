from pyparsing import col
import cv2
from matplotlib import pyplot as plt

f1 = cv2.imread('vtest-f1.jpg')
f1 = cv2.cvtColor(f1, cv2.COLOR_BGR2GRAY)

f2 = cv2.imread('vtest-f2.jpg')
f2 = cv2.cvtColor(f2, cv2.COLOR_BGR2GRAY)

result = abs(f1-f2)
hist = cv2.calcHist([result], [0],None, [256],[0,256])
print(hist[0])

plt.hist(f1.ravel(),256,[0,256])
plt.title('Histogram for gray scale image')
plt.show()
# cv2.imshow("result", result)
# cv2.waitKey(0)