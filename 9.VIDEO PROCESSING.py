import cv2
cap = cv2.VideoCapture("C:/Users/moni2/Desktop/video.mp4")
while True:
    ret, frame = cap.read()

    if not ret:
        print("Video ended or cannot read frame.")
        break
    frame = cv2.resize(frame, (640, 480))
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gray, 100, 200)
    cv2.imshow("Original Video", frame)
    cv2.imshow("Gray Video", gray)
    if cv2.waitKey(30) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
