import cv2
import numpy as np

# 250,0   500,250
# def click_event(event, x, y, flags, param):
#     if event == cv2.EVENT_LBUTTONDOWN:
#         print(x, " , ", y)
#         font = cv2.FONT_HERSHEY_SIMPLEX
#         strXY = str(x) + " , " + str(y)
#         cv2.putText(img, strXY, (x, y), font, .8, (255, 255, 255), 2)
# img = np.zeros((250, 500, 3), np.uint8)
# cv2.imshow("image", img)
# cv2.setMouseCallback('image', click_event)

img1 = np.zeros((250,500,3),np.uint8)
img1 = cv2.rectangle(img1,(200,0),(300,100),(255,255,255),-1)
img2 = np.zeros((250,500,3),np.uint8)
img2 = cv2.rectangle(img2, (250,0),(500,250),(255,255,255),-1)

# bit_and = cv2.bitwise_and(img2,img1)
bit_or = cv2.bitwise_or(img2,img1)
cv2.imshow('bit',bit_or)

cv2.imshow("img1",img1)
cv2.imshow("img2",img2)

cv2.imwrite("image_1.jpg", img2)


cv2.waitKey(0)
cv2.destroyAllWindows()
