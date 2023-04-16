import cv2
import numpy as np
height = 640
width = 480

#This will display all the available mouse click events
events = [i for i in dir(cv2) if 'EVENT' in i]
print(events)

#This variable we use to store the pixel location
refPt = []

#click event function
def click_event(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        count = 0
        print(count, ": ", x/height, ",", y/width)
        count += 1
        refPt.append([x, y])
        # font = cv2.FONT_HERSHEY_SIMPLEX
        # strXY = str(x)+", "+str(y)
        # cv2.putText(img, strXY, (x,y), font, 0.5, (255,255,0), 2)
        cv2.imshow("image", img)

#Here, you need to change the image name and it's path according to your directory
img = cv2.imread("data/img_1.png")
cv2.imshow("image", img)


#calling the mouse click event
cv2.setMouseCallback("image", click_event)

cv2.waitKey(0)
cv2.destroyAllWindows()

