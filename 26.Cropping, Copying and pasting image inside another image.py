import cv2

# Read main image
main_image = cv2.imread(r"C:/Users/moni2/Desktop/sunflower-png.jpg")

# Read image to paste
paste_image = cv2.imread(r"C:/Users/moni2/Desktop/mouse.jpg")

if main_image is None:
    print("Main image not found")
elif paste_image is None:
    print("Paste image not found")
else:
    # Resize paste image
    paste_image = cv2.resize(paste_image, (150, 150))

    h, w, _ = paste_image.shape

    # Paste at top-left corner
    main_image[0:h, 0:w] = paste_image

    cv2.imshow("Result", main_image)

    cv2.imwrite("output.jpg", main_image)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
