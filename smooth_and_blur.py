import cv2 as cv
import numpy as np

img = cv.imread('photos/Cats.jpg')
cv.imshow('cats',img)

#smmoth 


#Blur
#1 Averaging
average = cv.blur(img,(7,7))
cv.imshow('Average Blur',average)

# GaussianBlur
Gausian_blur = cv.blur(img,(7,7),0)
cv.imshow('Gausian_blur Blur',Gausian_blur)

#Median Blur
median = cv.medianBlur(img,7)
cv.imshow('Median Blur',median)

# Bilateral Blur
Bilateral_blur = cv.bilateralFilter(img,5,15,15)
cv.imshow('Bilateral Blur',Bilateral_blur)

cv.waitKey(0)