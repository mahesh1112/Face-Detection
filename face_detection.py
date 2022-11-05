import cv2 as cv
import os
import face_recognition

#for images

img = cv.imread("./rdj.jpg")
face_coordinates = face_recognition.face_locations(img)[0]
a,b,c,d = face_coordinates

cv.rectangle(img, (d,a), (b,c), (0,255,0), thickness = 2)

cv.imshow("window_name", img)
cv.waitKey(0)


#for real time 

cam = cv.VideoCapture(0)

while True:
  isTrue, frame = cam.read()
  face_coordinates = face_recognition.face_locations(frame)
  for a,b,c,d in face_coordinates:
    cv.rectangle(frame, (d,a),(b,c),(0,255,0), 3)
    cv.imshow("window_name", frame)
  k = cv.waitKey(0)
  
  if k == 27:
    break
 
cam.release()
cv.destroyAllWindows()
