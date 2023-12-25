import cv2 as cv
import numpy as np

img = cv.imread('photos/Cats.jpg')
cv.imshow('Cats',img)

blank = np.zeros(img.shape[:2],dtype='uint8')
cv.imshow('Blank',blank)

# Masking
mask = cv.circle(blank,(img.shape[1]//2,img.shape[0]//2),100,255,-1)
cv.imshow('Mask',mask)

mask1 = cv.rectangle(blank,(img.shape[1]//2,img.shape[0]//2),(img.shape[1]//2+100,img.shape[0]//2+100),255,-1)
cv.imshow('Mask',mask1)

masked_img = cv.bitwise_and(img,img,mask=mask)
cv.imshow('masked img',masked_img)


masked_img1 = cv.bitwise_and(img,img,mask=mask1)
cv.imshow('masked img1',masked_img1)


cv.waitKey(0)