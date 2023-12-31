import numpy as np
import cv2

cap = cv2.VideoCapture('vtest.avi')
fgbg = cv2.createBackgroundSubtractorMOG2(detectShadows= False)   # bgseg

while True:
    ret, frame = cap.read()
    if frame is None:
        break
    fgmask = fgbg.apply(frame)

    cv2.imshow("frame", frame)
    cv2.imshow("fgmask frame", fgmask)

    keyboard = cv2.waitKey(30)
    if keyboard == 'q' or keyboard == 27:
        break
cap.release()
cv2.destroyAllWindows()