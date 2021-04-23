# Face detection in photos by Haar Cascade
import cv2
import numpy as np
print(cv2.__version__)

# Use Haar Cascade method to detect faces
faceCascade = cv2.CascadeClassifier('Resources/haarcascade_frontalface_default.xml')
# Read image from file
img = cv2.imread('Resources/lena.png')
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces = faceCascade.detectMultiScale(imgGray, 1.1, 4)

for (x,y,w,h) in faces:
    cv2.rectangle(img, (x,y),(x+w,y+h),(255,0,0),2)

cv2.imshow('Faces Detected',img)
cv2.waitKey(0)
