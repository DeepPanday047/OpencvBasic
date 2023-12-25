import cv2 as cv 
import numpy as np 


img = cv.imread('photos/Cats.jpg')
cv.imshow('Cats',img)

gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('Gray',gray)

# simple Threshold 
thershold, thresh = cv.threshold(gray,127.5,255,cv.THRESH_BINARY)
cv.imshow('Simple Threshold ',thresh)

# Reverse Threshold 
thershold, thresh_inv = cv.threshold(gray,127.5,255,cv.THRESH_BINARY_INV)
cv.imshow('Reverse Threshold ',thresh_inv)

# adaptive Thresholds
adp_threshold = cv.adaptiveThreshold(gray,255.0,cv.ADAPTIVE_THRESH_MEAN_C,cv.THRESH_BINARY,11,3)
cv.imshow('Adaptive Thershold',adp_threshold)

cv.waitKey(0)