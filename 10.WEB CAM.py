import cv2
cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Error: Could not open the camera.")
    exit()

cv2.namedWindow("Webcam Video")

speed_factor = 1.0

while True:
    ret, frame = cap.read()

    if not ret:
        print("Error: Could not read frame.")
        break

    cv2.imshow("Webcam Video", frame)

    key = cv2.waitKey(1) & 0xFF

    if key == ord('+'):
        speed_factor += 0.5
        print(f"Speed Factor: {speed_factor}")

    elif key == ord('-'):
        speed_factor = max(0.5, speed_factor - 0.5)
        print(f"Speed Factor: {speed_factor}")

    elif key == ord('q'):
        break
    cap.set(cv2.CAP_PROP_FPS, 30 * speed_factor)
cap.release()
cv2.destroyAllWindows()
