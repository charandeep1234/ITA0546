import cv2

img = cv2.imread(r"C:/Users/moni2/Desktop/mouse.jpg", 0)

edges = cv2.Canny(img, 100, 200)
cv2.imshow("original image",img)
cv2.imshow("Outline", edges)
cv2.waitKey(0)
cv2.destroyAllWindows()
