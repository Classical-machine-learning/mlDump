import cv2 
import numpy as np

img = cv2.imread('sign.jpg')
# Resize

res = cv2.resize(img,None,fx=2,fy=2,interpolation=cv2.INTER_CUBIC)
cv2.imwrite('outputs/resized-1.jpg',res)

# Translation
img = cv2.imread('sign.jpg',0)
rows,cols = img.shape
M = np.float32([[1,0,100],[0,1,50]])
dst = cv2.warpAffine(img,M,(cols,rows))
cv2.imwrite('outputs/translated-1.jpg',dst)

# Rotation

M = cv2.getRotationMatrix2D((cols/2,rows/2),90,1)
dst = cv2.warpAffine(img,M,(cols,rows))
cv2.imwrite('outputs/Rotated-1.jpg',dst)

# Affine transformation

pts1 = np.float32([[50,50],[200,50],[50,200]])
pts2 = np.float32([[10,100],[200,50],[100,250]])
M = cv2.getAffineTransform(pts1,pts2)
dst = cv2.warpAffine(img,M,(cols,rows))
cv2.imwrite('outputs/affinetrans-1.jpg',dst)

# Perspective transformation

pts1 = np.float32([[56,65],[368,52],[28,387],[389,390]])
pts2 = np.float32([[0,0],[300,0],[0,300],[300,300]])
M = cv2.getPerspectiveTransform(pts1,pts2)
dst = cv2.warpPerspective(img,M,(300,300))
cv2.imwrite('outputs/perspetransf-1.jpg',dst)

