import cv2
face_haar_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

capture = cv2.VideoCapture(0)

while True:
    ret, frame = capture.read()
    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)


    faces = face_haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=4)

    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)


    cv2.imshow('Face Detection', frame)


    if cv2.waitKey(1) & 0xFF == 27 or cv2.getWindowProperty('Face Detection', cv2.WND_PROP_VISIBLE) < 1:
     break

capture.release()
cv2.destroyAllWindows()
