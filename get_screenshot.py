import cv2 as cv
import os

name = str(input("Enter your name: "))
cam = cv.VideoCapture(0)
path = "./"
while True:
    isTrue, frame = cam.read()
    cv.imshow("window_name", frame)
    k = cv.waitKey(1)
    if k == 27:
        break
    elif k == 32:
        cv.imwrite(os.path.join(path, f"{name}.png"), frame)
cam.release()
cv.destroyAllWindows()
