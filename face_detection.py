import cv2 as cv
import os
import face_recognition

#for images

img = cv.imread("./rdj.jpg")
face_coordinates = face_recognition.face_locations[0]
(a,b,c,d) = face_coordinates

cv.rectangle(img, (d,a), (b,c), (0,255,0), thickness = 2)

cv.imshow("window_name", img)
cv.waitKey(0)
