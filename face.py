import cv2

face_cap = cv2.CascadeClassifier("C:/Users/RITIK/AppData/Local/Programs/Python/Python310/Lib/site-packages/cv2/data/haarcascade_frontalcatface_extended.xml")
video_cap = cv2.VideoCapture(0)

while True:
    ret, video_data = video_cap.read()

    faces = face_cap.detectMultiScale(
        video_data,
        scaleFactor=1.1,
        minNeighbors=5,
        flags=cv2.CASCADE_SCALE_IMAGE
    )

    for (x, y, w, h) in faces:
        cv2.rectangle(video_data, (x, y), (x+w, y+h), (0, 255, 0), 2)

    cv2.imshow("video_live", video_data)
    if cv2.waitKey(1) & 0xFF == ord('x'):
        break

video_cap.release()
cv2.destroyAllWindows()
