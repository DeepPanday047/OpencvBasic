import cv2 as cv

img  = cv.imread('photos/park.jpg')
cv.imshow('Park_ori',img)

#1 converting to grayscale
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('Gray',gray)

#2 Blur
blur = cv.GaussianBlur(img,(7,7),cv.BORDER_DEFAULT)
cv.imshow('Blur',blur)

#3 Edge cascades
canny = cv.Canny(img,125,175)
cv.imshow('Canny edges',canny)

canny = cv.Canny(blur,125,175)
cv.imshow('Canny edges',canny)

#4 Dilating the Image
dilated = cv.dilate(canny,(3,3),iterations=1)
cv.imshow('dialated Image',dilated)

#5 edroding
edroded =cv.erode(dilated,(3,3),iterations=1)
cv.imshow('Edroded Images',edroded)

# Resize and Crop
resized = cv.resize(img,(500,500),interpolation=cv.INTER_CUBIC)
cv.imshow('Resized Img',resized)

# Croping
cropped = img[50:200,200:400]
cv.imshow('Cropped',cropped)













cv.waitKey(0)