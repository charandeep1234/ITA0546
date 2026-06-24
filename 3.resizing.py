import cv2
import numpy as np
kernel=np.ones((5,5),np.uint8)
img=cv2.imread("C:/Users/moni2/Desktop/forest.jpg")
cv2.imshow("original image",img)
cv2.waitKey(0)
img=cv2.resize(img,(300,300))
cv2.imshow("image",img)
cv2.waitKey(0)
