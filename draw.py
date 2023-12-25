import cv2 as cv
import numpy as np


# img = cv.imread('photos/cat.jpg')
# cv.imshow('cat',img)
blank = np.zeros((500,500,3),dtype='uint8')
# blank[200:300,300:400] = 0,0,255
# cv.imshow('blank_img_green_square',blank)


# draw a rectangle
# cv.rectangle(blank,(0,0),(blank.shape[1]//2,blank.shape[0]//2),(255,0,0),thickness=-1)
# cv.imshow('Rectangle',blank)

# draw circle
# cv.circle(blank,(blank.shape[1]//2,blank.shape[0]//2),40,(0,0,255),thickness=-1)
# cv.imshow('Circle',blank)


# draw a line

# cv.line(blank,(0,0) ,(blank.shape[1]//2,blank.shape[0]//2),color=(255,255,255),thickness=3)
# cv.imshow('Line',blank)


# write text
cv.putText(blank,'Hello Deep is here!!',(255,255),fontFace=cv.FONT_HERSHEY_TRIPLEX,fontScale=1.0,color=(0,255,0),thickness=2)
cv.imshow('Text',blank)

cv.waitKey(0)