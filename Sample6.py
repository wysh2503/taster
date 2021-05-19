# Track a color by masking out unwanted colors and draw bounding boxes around each of them
import cv2
import numpy as np

def nothing(): pass

cv2.namedWindow('Trackbars')

cv2.createTrackbar('HueLow','Trackbars',24,179,nothing)
cv2.createTrackbar('HueHigh','Trackbars',86,179,nothing)
cv2.createTrackbar('SatLow','Trackbars',139,255,nothing)
cv2.createTrackbar('SatHigh','Trackbars',255,255,nothing)
cv2.createTrackbar('ValLow','Trackbars',122,255,nothing)
cv2.createTrackbar('ValHigh','Trackbars',255,255,nothing)


# Set up webcam
cam = cv2.VideoCapture(1)

# Start capturing and show frames on window
while True:
    success, img = cam.read()
    img = cv2.resize(img, (int(img.shape[1]/0.5),int(img.shape[0]/0.5))

    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    hueLow = cv2.getTrackbarPos('HueLow','Trackbars')
    hueHigh = cv2.getTrackbarPos('HueHigh', 'Trackbars')
    satLow = cv2.getTrackbarPos('SatLow', 'Trackbars')
    satHigh = cv2.getTrackbarPos('SatHigh', 'Trackbars')
    valLow = cv2.getTrackbarPos('ValLow', 'Trackbars')
    valHigh = cv2.getTrackbarPos('ValHigh', 'Trackbars')

    FGmask = cv2.inRange(hsv, (hueLow,satLow,valLow),(hueHigh,satHigh,valHigh))
    cv2.imshow('FGmask',FGmask)
    
    # Use findContours to get contours around each object
    contours, hierarchy = cv2.findContours(FGmask,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    contours = sorted(contours,key=lambda x:cv2.contourArea(x),reverse=True)
    for cnt in contours:
        area = cv2.contourArea(cnt)
        (x,y,w,h) = cv2.boundingRect(cnt)
        if area > 100:
            #cv2.drawContours(img,[cnt],0,(255,0,0),3)
            cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),3)

    cv2.imshow('Frame', img)
    if cv2.waitKey(1) & 0xff == 27:
        break

cam.release()
cv2.destroyAllWindows()
