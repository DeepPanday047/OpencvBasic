import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img = cv.imread('photos/park.jpg')
cv.imshow('BGR',img)

# BGR To Gray
# gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
# cv.imshow('Gray',gray)

# #BGR to HSV
# hsv = cv.cvtColor(img,cv.COLOR_BGR2HSV)
# cv.imshow('HSV',hsv)

# BGR To LAB
lab = cv.cvtColor(img,cv.COLOR_BGR2LAB)
cv.imshow('LAB',lab)

#BGR To RGB
# rgb = cv.cvtColor(img,cv.COLOR_BGRA2RGB)
# cv.imshow('RGB',rgb)

# display the rgb img to convert it into original img
# plt.imshow(rgb)
# plt.title('RGB TO BGR')
# plt.show()

# Inverse of all 
# HSV to BGR
# hsv_bgr = cv.cvtColor(hsv,cv.COLOR_HSV2BGR)
# cv.imshow('HSV To BGR',hsv_bgr)

# LAB to BGR
lab_bgr = cv.cvtColor(lab,cv.COLOR_LAB2BGR)
cv.imshow('LAB To BGR',lab_bgr)

cv.waitKey(0)