import cv2

file_path = r"C:\Users\Blu-Ray\Downloads\Video\BRAVO.mp4"

cap = cv2.VideoCapture(file_path)

while True:
    ret, frame = cap.read()
    if not ret:
        break
    cv2.imshow("Video Player", frame)
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
