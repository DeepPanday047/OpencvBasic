import cv2 as cv

#Load the image and convey to grayscale
img = cv.imread('imagemain.jpg')
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)

#Initialize SIFT and SURF detectorscls
sift = cv.SIFT_create()
#surf = cv.xfeatures2d.SURF_create()

# Detect key points and compute descriptors
keypoints_sift, descriptors_sift = sift.detectAndCompute(img,None)
# keypoints_surf, descriptors_surf = surf.detectAndCompute(img,None)
cv.imshow('image',img)

# Initialize SIFT detector
sift = cv.SIFT_create()
sift.setContrastThreshold(0.25)
sift.setEdgeThreshold(5)

# Detect key points and compute descriptors
keypoints, descriptors = sift.detectAndCompute(img, None)
for x in keypoints:
    print("({:.2f},{:.2f}) = size {:.2f} angle {:.2f}".format(x.pt[0], x.pt[1], x.size, x.angle))

img_kp = cv.drawKeypoints(img, keypoints, None, flags=cv.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
cv.imshow("Keypoints", img_kp)
cv.waitKey(0)
cv.destroyAllWindows()
