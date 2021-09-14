import cv2
from cvzone.HandTrackingModule import HandDetector

cap = cv2.VideoCapture(0)
cap.set(3,1280)
cap.set(4,720)
handDetector = HandDetector(detectionCon=0.8)

while True:
    status, img = cap.read()
    img = cv2.flip(img,1)
    img = handDetector.findHands(img)
    list, _ = handDetector.findPosition(img)

    cv2.circle(img, (300,300), 100, (100,255,100),cv2.FILLED)

    cv2.imshow("Hand image", img)
    cv2.waitKey(1)