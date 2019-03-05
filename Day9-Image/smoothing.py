import cv2
import numpy as np
from matplotlib import pyplot as plt

# 2d conv
img = cv2.imread('sign.jpg')
kernel = np.ones((5,5),np.float32)/25
dst = cv2.filter2D(img,-1,kernel)
cv2.imwrite('outputs/2dconv-1.jpg',dst)

# Averaging
blur = cv2.blur(img,(5,5))
cv2.imwrite('outputs/averaging-1.jpg',blur)

# Gaussian Blur
blur = cv2.GaussianBlur(img,(5,5),0)
cv2.imwrite('outputs/Gaussian-1.jpg',blur)

# Median Blur
median = cv2.medianBlur(img,5)
cv2.imwrite('outputs/median-1.jpg',median)

# Bilateral
blur = cv2.bilateralFilter(img,9,75,75)
cv2.imwrite('outputs/bilateral-1.jpg',blur)
    
