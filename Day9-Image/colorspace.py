import cv2
import numpy as np

cap = cv2.imread('sign.jpg')
hsv = cv2.cvtColor(cap,cv2.COLOR_BGR2HSV)
lower_blue = np.array([110,50,50])
upper_blue = np.array([130,255,255])
mask = cv2.inRange(hsv,lower_blue,upper_blue)
res = cv2.bitwise_and(cap,cap,mask = mask)

cv2.imwrite('outputs/thresholdblue-1.png',res)