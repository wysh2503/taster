# Read a static image and stream frames from webcam
import cv2
import numpy as np
print(cv2.__version__)

#------------------------------------------------------------------
# This part reads static image and test on different image processing
kernel = np.ones((5,5),np.uint8)

img = cv2.imread('Resources/lena.png')
# img = cv2.resize(img, (int(img.shape[1]/1.5),int(img.shape[0]/1.5)))
cv2.imshow('Lena',img)

# imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# cv2.imshow('Gray Image', imgGray)

# imgBlur = cv2.GaussianBlur(imgGray, (5,5), 0)
# cv2.imshow('Blur', imgBlur)

# imgCanny = cv2.Canny(img, 100, 100)
# cv2.imshow('Canny', imgCanny)

# imgDilation = cv2.dilate(imgCanny, kernel, iterations=1)
# cv2.imshow('Dilate', imgDilation)

cv2.waitKey(0)
#------------------------------------------------------------------
# This part stream frames from webcam
# Read image from webcam
# capture = cv2.VideoCapture(1)
# capture.set(3,640)
# capture.set(4,480)
#
# while True:
#     success, img = capture.read()
#     cv2.imshow('Frame', img)
#     cv2.moveWindow('Frame', 100,20)
#     if cv2.waitKey(20) & 0xff == ord('q'):
#         break
#
# capture.release()
# cv2.destroyAllWindows()


