import cv2
from cvzone.HandTrackingModule import HandDetector

cap = cv2.VideoCapture(0)
cap.set(3, 1280)
cap.set(4, 720)
handDetector = HandDetector(detectionCon=0.8)

circleColor = 100, 255, 100
circleX, circleY, circleRad = 500, 200, 100

while True:
    status, img = cap.read()
    img = cv2.flip(img, 1)
    img = handDetector.findHands(img, draw=False)
    list, _ = handDetector.findPosition(img, draw=False)

    if list:
        fingerDistance, _, _ = handDetector.findDistance(8, 12, img, draw=False)

        if fingerDistance <32:
            fingerPoint = list[8]
            if (circleX - circleRad) < fingerPoint[0] < (circleX + circleRad) and \
                    (circleY - circleRad) < fingerPoint[1] < (circleY + circleRad):
                circleColor = 0, 0, 255
                circleX, circleY = fingerPoint

        else:
            circleColor = 100, 255, 100


    cv2.circle(img, (circleX,circleY), circleRad, circleColor,cv2.FILLED)

    cv2.imshow("Hand image", img)
    cv2.waitKey(1)