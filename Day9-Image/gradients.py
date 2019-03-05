import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('sign.jpg',0)
laplacian = cv2.Laplacian(img,cv2.CV_64F)
sobelx = cv2.Sobel(img,cv2.CV_64F,1,0,ksize=5)
sobely = cv2.Sobel(img,cv2.CV_64F,0,1,ksize=5)

cv2.imwrite('outputs/laplacian-1.jpg',laplacian)
cv2.imwrite('outputs/sobelx-1.jpg',sobelx)
cv2.imwrite('outputs/sobely-1.jpg',sobely)
