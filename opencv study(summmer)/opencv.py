import numpy as np
import cv2

img =cv2.imread('da.JPG')
face_cascade=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

if(type(img) is np.ndarray):
    gray=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces=face_cascade.detectMultiScale(gray, 1.3, 5)

    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x+w, y+h), (25, 25, 100), 2)

    cv2.imshow('result', img)
    cv2.waitKey(0)

