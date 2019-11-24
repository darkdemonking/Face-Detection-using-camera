__author__ = 'Vaibhav Punia'

import cv2

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

cap = cv2.VideoCapture(0)

if (cap.isOpened()== False):
  print("Error opening video stream or file")

while True:
    font = cv2.FONT_HERSHEY_SIMPLEX
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    faces = detector.detectMultiScale(gray, 1.2,5)
    for (x,y,w,h) in faces:
        cv2.rectangle(img, (x,y),(x+w,y+h),(0,255,0),2)
        cv2.putText(img, 'Face', (x+70, y-20), font, 0.7, (0, 255, 5), 2)


    cv2.putText(img, 'Press q to exit', (10, 30), font, 0.7, (0, 255, 5), 2)

    cv2.imshow("frame",img)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cv2.destroyAllWindows()
