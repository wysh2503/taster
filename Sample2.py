# Below code stream frames from webcam and display it on 'Frame'
import cv2
import numpy as np
print(cv2.__version__)

# Set up webcam. If no frame is shown, try (0) or (2)
capture = cv2.VideoCapture(1)
capture.set(3,640)
capture.set(4,480)

# Start capturing and show frames on window
while True:
    success, img = capture.read()
    cv2.imshow('Frame', img)
#     cv2.moveWindow('Frame', 100,20)
    if cv2.waitKey(20) & 0xff == ord('q'):
        break

capture.release()
cv2.destroyAllWindows()
