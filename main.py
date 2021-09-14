import cv2
from cvzone.HandTrackingModule import HandDetector

cap = cv2.VideoCapture(0)
cap.set(3,1280)
cap.set(4,720)
handDetector = HandDetector(detectionCon=0.8)

while True:
    status, img = cap.read()
    img = handDetector.findHands(img)
    list, _ = handDetector.findPosition(img)

    cv2.imshow("Hand image", img)
    cv2.waitKey(1)