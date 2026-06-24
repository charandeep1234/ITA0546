
import cv2
import numpy as np
image = cv2.imread("C:/Users/moni2/Desktop/mouse.jpg")
x, y = 0, 0
dx, dy = 5, 3

height, width = image.shape[:2]

while True:
    canvas = np.zeros((600, 800, 3), dtype=np.uint8)
    x += dx
    y += dy
    if x <= 0 or x + width >= 800:
        dx = -dx

    if y <= 0 or y + height >= 600:
        dy = -dy
    canvas[y:y+height, x:x+width] = image

    cv2.imshow("Moving Image", canvas)
    if cv2.waitKey(30) & 0xFF == 27:
        break

cv2.destroyAllWindows()
