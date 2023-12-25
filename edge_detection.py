import cv2 as cv 
import numpy as np 

img = cv.imread('photos/cats.jpg')
cv.imshow('Cats', img)

gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('Gray',gray)

# Laplaction
Lap = cv.Laplacian(gray,cv.CV_64F)
Lap = np.uint8(np.absolute(Lap))
cv.imshow('Laplaction',Lap)

#Sobel
sobelx = cv.Sobel(gray,cv.CV_64F, 1, 0)
sobely = cv.Sobel(gray,cv.CV_64F, 0, 1)

cv.imshow('Sobel X',sobelx)
cv.imshow('Sobel Y',sobely)



cv.waitKey(0)