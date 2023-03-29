import cv2
import face_recognition

my_img = cv2.imread("Resources/Result.jpg")
my_img_enc = face_recognition.face_encodings(my_img)

cap = cv2.VideoCapture(0)

recognizer_cc = cv2.CascadeClassifier('/home/asus/FaceDetect/venv/lib/python3.8/site-packages/cv2/data/haarcascade_frontalface_default.xml')

process_this_frame = True
while True:
    ret, img = cap.read()
    # if process_this_frame:
    small_img = cv2.resize(img, (0, 0), fx=0.25, fy=0.25)
    gray = cv2.cvtColor(small_img, cv2.COLOR_BGR2GRAY)


        # recognize = recognizer_cc.detectMultiScale(small_img, scaleFactor = 2, minNeighbors = 3)
    recognize = face_recognition.face_locations(small_img)
    print(recognize)
    for (top, right, bottom, left) in recognize:
        top *= 4
        right *= 4
        bottom *= 4
        left *= 4
        cv2.rectangle(img, (left, top), (right, bottom), (0, 0, 255), 2)

    process_this_frame = not process_this_frame

    # print(recognize)

    cv2.imshow("camera", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break