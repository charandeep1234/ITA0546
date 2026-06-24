
import cv2
import numpy as np
img1 = cv2.imread("C:/Users/moni2/Desktop/mouse.jpg")
img2 = cv2.imread("C:/Users/moni2/Desktop/mouse.jpg")
pts1 = np.array([[50, 50], [200, 50], [50, 200], [200, 200]], dtype=np.float32)
pts2 = np.array([[100, 100], [300, 100], [100, 300], [300, 300]], dtype=np.float32)
H, status = cv2.findHomography(pts1, pts2)
dst = cv2.warpPerspective(img1, H, (img2.shape[1], img2.shape[0]))
cv2.imshow('Original Image', img1)
cv2.imshow('Warped Image', dst)

cv2.waitKey(0)
cv2.destroyAllWindows()
