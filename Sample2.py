# Below code stream frames from webcam and display it on 'Frame'
import cv2
import numpy as np
print(cv2.__version__)

# Set up webcam. If no frame is shown, try (0) or (2)
cam = cv2.VideoCapture(1)
# cam.set(3,640)
# cam.set(4,480)

# Start capturing and show frames on window
while True:
    success, img = cam.read()
    cv2.imshow('Frame', img)
    if cv2.waitKey(1) & 0xff == 27:
        break

cam.release()
cv2.destroyAllWindows()
