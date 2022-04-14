import cv2
sample = cv2.VideoCapture('vtest.mp4')
print("Jumlah Frame menurut property:", sample.get(cv2.CAP_PROP_FRAME_COUNT))
counter = 0
# cv2.imwrite('vtest-f1.jpg',sample.read()[1])
# cv2.imwrite('vtest-f2.jpg',sample.read()[1])
while sample.isOpened():
  ret, frame = sample.read()
  if ret == True:
    cv2.imshow('Sample', frame)
    counter +=1
    cv2.waitKey(0)
  else:
    break
print("Jumlah Frame dengan cara menghitung: ",counter)
sample.release()
cv2.destroyAllWindows()
