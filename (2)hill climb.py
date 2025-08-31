import cv2
from cvzone.HandTrackingModule import HandDetector
import pyautogui

# Initialize detector
detector = HandDetector(detectionCon=0.5, maxHands=2)

# Open webcam (use 0 for default camera, change if needed)
cap = cv2.VideoCapture(0)
cap.set(3, 600)
cap.set(4, 400)

while True:
    success, img = cap.read()
    img = cv2.flip(img, 1)

    # detect hands
    hands, img = detector.findHands(img)  # returns list of hands + image

    if hands and hands[0]["type"] == "Left":   # check if left hand detected
        fingers = detector.fingersUp(hands[0])
        totalFingers = fingers.count(1)

        # show fingers count on screen
        cv2.putText(img, f'Fingers: {totalFingers}', (50, 50),
                    cv2.FONT_HERSHEY_PLAIN, 2, (0, 255, 0), 2)

        # control arrows
        if totalFingers == 5:
            pyautogui.keyDown("right")
            pyautogui.keyUp("left")

        elif totalFingers == 0:
            pyautogui.keyDown("left")
            pyautogui.keyUp("right")

    cv2.imshow('Camera Feed', img)

    # exit on ESC key
    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()
