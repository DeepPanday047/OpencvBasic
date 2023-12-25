import cv2 as cv
import numpy as np

yolo = cv.dnn.readNet('yolov3.weights','yolov3.cfg')
classes = []

with open('Yolo v5/coco.names','r') as file:
    classes = [line.strip() for line in file.readlines()]
layer_names = yolo.getLayerNames()
output_layers = [layer_names[i[0] -1] for i in yolo.getLayerNames]

colorRed  = (0,0,255)
colorGreen = (0,255,0)

## Loading Images
name = 'image.jpg'
img = cv.imread(name)
height, width, channels = img.shape

# Detecting obects
blob = cv.dnn.blobFromImage(img,0.00392,(416,416), (0,0,0), True,crop=False)

# yolo.setInpt(blob)
outputs = yolo.forward(output_layers)

class_ids = []
confidences = []
boxes = []
for output in outputs:
    for detection in output:
        scores = detection[5:]
        class_id = np.argmax(scores)
        confidence = scores[class_ids]

        if confidence >0.5:
           center_x = int(detection[0] * width)
           center_y = int(detection[1] * height)
           w = int(detection[2] * width)
           h = int(detection[3] * height) 

           x = int(center_x - w / 2)
           y = int(center_y - h / 2)

           boxes.append([x, y, w, h])
           confidences.append(float(confidence))
           class_ids.append(class_id)

indexs = cv.dnn.NMSBoxes(boxes, confidences, 0.5, 0.4)
print(len(boxes))
print(len(indexs))
for i in range(len(boxes)):
    if i in indexs:
        x, y, w, h = boxes[i]
        label = str([class_ids[i]])
        cv.rectangle(img,(x,y),(x+w,y+h),  colorGreen, 3)
        cv.putText(img, label, (x, y + 10), cv.FONT_HERSHEY_PLAIN, 8, colorRed, 8)


# cv.imshow("Image", img)
# cv.imwrite("output.jpg",img)
cv.waitKey(0)
cv.destroyAllWindows()

