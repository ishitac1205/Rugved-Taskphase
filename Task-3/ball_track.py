

import cv2 as cv
import numpy as np

path = "/Users/ishitachoudhary/Desktop/Student Projects/Rugved/opencv_task/Ball_Tracking.mp4"
capture = cv.VideoCapture(path)

low_thresh = np.array([40, 40, 40])  
up_thresh= np.array([70, 255, 255])

while True:
    isTrue, frame = capture.read()
    if not isTrue:
        print("End of video or cannot read frame.")
        break
        
    if frame is None:
        print('frame is none')

    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
    mask = cv.inRange(hsv, low_thresh, up_thresh)
    cv.imshow("Mask", mask)

    contours, _ = cv.findContours(mask, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
    #cv.RETR_EXTERNAL for ignoring nested contours
    largest_contour = max(contours, key=cv.contourArea)
    #we find the contour with largest area

    #minimum enclosing circle around that area
    (x, y), radius = cv.minEnclosingCircle(largest_contour)
    center_x, center_y = int(x), int(y)
    radius = int(radius)  

    cv.circle(frame, (center_x, center_y), radius, (0, 255, 0), 2)

    cv.imshow('Tracked ball',frame)
    if cv.waitKey(1) & 0xFF == ord('q'):
        break


    

capture.release()
cv.destroyAllWindows()  

