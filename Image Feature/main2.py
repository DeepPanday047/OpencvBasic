
import cv2
 
# Load the image and convery to grayscale
img = cv2.imread('imagemain.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
 
# Initialize SIFT detector
sift = cv2.SIFT_create()
sifcls\t.setContrastThreshold(0.25)
sift.setEdgeThreshold(5)
 
# Detect key points and compute descriptors
keypoints, descriptors = sift.detectAndCompute(img, None)
for x in keypoints:
    print("({:.2f},{:.2f}) = size {:.2f} angle {:.2f}".format(x.pt[0], x.pt[1], x.size, x.angle))
 
img_kp = cv2.drawKeypoints(img, keypoints, None, flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
cv2.imshow("Keypoints", img_kp)
cv2.waitKey(0)
cv2.destroyAllWindows()