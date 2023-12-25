import cv2 as cv 

img = cv.imread('photos/group 2cls.jpg')
cv.imshow('Group',img)

# gray 
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('Gray Group',gray)

haar_cascade = cv.CascadeClassifier('face_detection.xml')

faces_rect = haar_cascade.detectMultiScale(gray,scaleFactor=1.1,minNeighbors=3)
print('No of faces found = ',len(faces_rect))

for (x,y,w,h) in faces_rect:
    cv.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
    cv.imshow('Detected faces',img)

cv.waitKey(0)