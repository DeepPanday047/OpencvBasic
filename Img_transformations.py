import cv2 as cv
import numpy as np

img = cv.imread('photos/lady.jpg')
cv.imshow('Lady',img)

# Translation
def translate(img,x,y):
    transMat = np.float32([[1,0,x],[0,1,y]])
    dimensions = (img.shape[1],img.shape[0])
    return cv.warpAffine(img,transMat,dimensions)

# -x--> left
# x--> Right
# -y--> up
# y--> down

translaed = translate(img,100,100)
cv.imshow('Translated Img(Right to down)',translaed)

translaed2 = translate(img,-100,100)
cv.imshow('Translated Img(left to down)',translaed2)

translaed3 = translate(img,100,-100)
cv.imshow('Translated Img(right to up)',translaed3)

translaed4 = translate(img,-100,-100)
cv.imshow('Translated Img(left to up)',translaed4)

#Rotation
def rotate(img,angle,rotPoint=None):
    (height,width) = img.shape[:2]

    if rotPoint is None:
        rotPoint = (width//2,height//2)
    rotMat = cv.getRotationMatrix2D(rotPoint,angle,1.0)
    dimensions = (width,height)

    return cv.warpAffine(img,rotMat,dimensions)

rotated = rotate(img,-45)
cv.imshow('Rotated',rotated)

rotated_rotated = rotate(rotated,-45)
cv.imshow('Rotated rotated',rotated_rotated)

#Resize 
resized =  cv.resize(img,(500,500),interpolation=cv.INTER_CUBIC)
cv.imshow('Resized',resized)

# Flipping 
# 0 --> vertical flip
# 1 --> Horizontally
# -1 --> bot vertically and horizontally

flip = cv.flip(img,0)
cv.imshow("Flip Vertically",flip)

flip1 = cv.flip(img,1)
cv.imshow("Flip Horizontally",flip1)

flip2 = cv.flip(img,-1)
cv.imshow("Flip Vertically and Horizontally",flip2)

# cropping

crop = img[200:400,300:400]
cv.imshow('Cropped Img',crop)

cv.waitKey(0)