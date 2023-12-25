import cv2 as cv

def rescaleFrame(frame,scale=0.75):
# works onImages,videos
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width,height)

    return cv.resize(frame,dimensions,interpolation=cv.INTER_AREA)

# resize and ori img
img = cv.imread('photos/cat.jpg')
resized_img = rescaleFrame(img)
cv.imshow('Ori_cat',img)
cv.imshow('Resize_Cat', resized_img)
 
# change resolutions
# works on live videos
def changeres(width,height):
    capture.set(3,width)
    capture.set(4,height)

# Resize and ori Videos
capture = cv.VideoCapture('videos/dog.mp4')
while True:
    isTrue,frame = capture.read()
    frame_resized = rescaleFrame(frame,scale=0.2)
    cv.imshow('ori_video',frame)
    cv.imshow('video Resized',frame_resized)
    if cv.waitKey(20) & 0xFF == ord('q'):
        break

capture.release()
cv.destroyAllWindows()
