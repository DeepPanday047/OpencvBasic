import cv2 as cv 
import numpy as np
import matplotlib.pyplot as plt

img = cv.imread('photos/cats.jpg')
cv.imshow('Cats',img)

blank = np.zeros(img.shape[:2],dtype='uint8')

#convert gray
# gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
# cv.imshow('Gray',gray)

mask = cv.circle(blank,(img.shape[1]//2,img.shape[0]//2),100,255,-1)
cv.imshow('Circle',mask)

masked = cv.bitwise_and(img,img,mask=mask)
cv.imshow('Mask',masked)

# Grayscale Histogram 
# gray_hist = cv.calcHist([gray],[0],mask,[256],[0,256])
# plt.figure()
# plt.title('Grayscale Histogram')
# plt.xlabel('Bins')
# plt.ylabel('No of Pixels')
# plt.plot(gray_hist)
# plt.xlim([0,256])



plt.figure()
plt.title('Colored Histogram')
plt.xlabel('Bins')
plt.ylabel('No of Pixels')
# colour Histogram
colors = ('b','g','r')
for i,col in enumerate(colors):
    hist = cv.calcHist([img],[i],mask,[256],[0,256])
    plt.plot(hist,color=col)
    plt.xlim([0,256])

plt.show()


cv.waitKey(0)
