import cv2 as cv 
import numpy as np


# Load the necessary Files
haar_cascade = cv.CascadeClassifier('face_detection.xml')
people = ['Ben Afflek','Elton John','Jerry Seinfield','Madonna','Mindy Kaling']
# features = np.load('features.npy',allow_pickle=True)
# labels = np.load('labels.npy')

#
face_reconizer = cv.face.LBPHFaceRecognizer_create()
face_reconizer.read('face_trained.xml')

img = cv.imread(r'C:\\Users\\Dell\\Desktop\\opencv\\Faces\\val\\elton_john\\2.jpg')
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('Person',gray)

# detect the face in the image

faces_rect = haar_cascade.detectMultiScale(gray,1.1,4)
for (x,y,w,h) in faces_rect:
    faces_roi = gray[y:y+h,x:x+h]

    label, confidence = face_reconizer.predict(faces_roi)
    print(f'label = {people[label]} with a confidence of {confidence}')

    cv.putText(img,str(people[label]),(20,20),cv.FONT_HERSHEY_COMPLEX,1.0,(0,255,0),2)
    cv.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)

    cv.imshow('Detected Image',img)

    cv.waitKey(0)


