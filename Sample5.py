import cv2
import numpy as np

# Create some trackbars to adjust HSV values
def nothing(): pass

cv2.namedWindow('Trackbars')

cv2.createTrackbar('HueLow','Trackbars',0,179,nothing)
cv2.createTrackbar('HueHigh','Trackbars',150,179,nothing)
cv2.createTrackbar('SatLow','Trackbars',0,255,nothing)
cv2.createTrackbar('SatHigh','Trackbars',255,255,nothing)
cv2.createTrackbar('ValLow','Trackbars',0,255,nothing)
cv2.createTrackbar('ValHigh','Trackbars',255,255,nothing)


# Given a color photo, adjust the HSV values to mask out unwanted colors
while True:
    # success, img = cam.read()
    img = cv2.imread('Resources/smarties.png')
    cv2.imshow('Frame', img)
    # Change color space to HSV
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    # get different trackbars values
    hueLow = cv2.getTrackbarPos('HueLow','Trackbars')
    hueHigh = cv2.getTrackbarPos('HueHigh', 'Trackbars')
    satLow = cv2.getTrackbarPos('SatLow', 'Trackbars')
    satHigh = cv2.getTrackbarPos('SatHigh', 'Trackbars')
    valLow = cv2.getTrackbarPos('ValLow', 'Trackbars')
    valHigh = cv2.getTrackbarPos('ValHigh', 'Trackbars')

    # Mask out unwanted colors
    FGmask = cv2.inRange(hsv, (hueLow,satLow,valLow),(hueHigh,satHigh,valHigh))
    cv2.imshow('FGmask',FGmask)

    FG = cv2.bitwise_and(img,img,mask=FGmask)
    cv2.imshow('FG', FG)

    BGmask = cv2.bitwise_not(FGmask)
    cv2.imshow('BGmask', BGmask)

    BG = cv2.cvtColor(BGmask,cv2.COLOR_GRAY2BGR)

    finalImg = cv2.add(FG,BG)
    cv2.imshow('FinalImage', finalImg)

    if cv2.waitKey(1) & 0xff == ord('q'):
        break

cv2.destroyAllWindows()
