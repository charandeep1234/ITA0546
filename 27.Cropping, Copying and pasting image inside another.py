import cv2
img1 = cv2.imread("C:/Users/moni2/Desktop/sunflower.png.jpg")  
img2 = cv2.imread("C:/Users/moni2/Desktop/mouse.jpg") 
if img1 is None or img2 is None:
    print("Error: Image not found!")
    exit()
cropped = img1[50:250, 50:250]
cv2.imwrite("cropped_image.jpg", cropped)
cropped = cv2.resize(cropped, (200, 200))
img2[100:300, 100:300] = cropped
cv2.imwrite("pasted_image.jpg", img2)
cv2.imshow("Original Image 1", img1)
cv2.imshow("Cropped Image", cropped)
cv2.imshow("Image with Pasted Region", img2)

cv2.waitKey(0)
cv2.destroyAllWindows()
