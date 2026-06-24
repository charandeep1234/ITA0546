import cv2
import numpy as np

img = cv2.imread("C:/Users/moni2/Desktop/mouse.jpg")

M = np.float32([[1, 0, 50],   # move 50 px right
                [0, 1, 30]])  # move 30 px down

translated = cv2.warpAffine(img, M, (img.shape[1], img.shape[1]))
cv2.imshow("original image",img)
cv2.imshow("Translated", translated)
cv2.waitKey(0)
cv2.destroyAllWindows()
