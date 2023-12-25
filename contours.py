import cv2 as cv
import numpy as np 

img = cv.imread('photos/cats.jpg')
cv.imshow('Cats',img)

blank = np.zeros(img.shape,dtype='uint8')
cv.imshow('Blank',blank)
# grayscale
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('Gray',gray)

# #blur
# Blur = cv.GaussianBlur(gray,(7,7),cv.BORDER_DEFAULT)
# cv.imshow('Blur',Blur)
# # canny edge
# canny = cv.Canny(Blur,125,175)
# cv.imshow('CANNY EDGE',canny)

ret , thresh = cv.threshold(gray,125,255,cv.THRESH_BINARY)
cv.imshow('Thresh',thresh)

#contours 
contours, hierarchies = cv.findContours(thresh,cv.RETR_LIST,cv.CHAIN_APPROX_SIMPLE)
print(f'{len(contours)} length founds')

contours_drawn = cv.drawContours(blank,contours,-1,(0,0,255),2)
cv.imshow('Contours drawn',contours_drawn)
cv.waitKey(0)