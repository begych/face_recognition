# import os
# import cv2
# import pickle5 as pickle
# import face_recognition
#
# # with open("Data/database.pickle", "rb") as f:
# #     database = pickle.load(f)
#
# # data = database[0]
# # known_face_encodings = data["encodings"]
#
#
# img1 = cv2.imread("Faces_in/face_in_0.jpg")
# img2 = cv2.imread("Faces_in/hasbik.jpg")
#
# face_locations1 = face_recognition.face_locations(img1)
# face_encodings1 = face_recognition.face_encodings(img1,face_locations1)[0]
# # face_encodings = [face_encodings1]
#
# face_locations2 = face_recognition.face_locations(img2)
# face_encodings2 = face_recognition.face_encodings(img2, face_locations2)
# # face_encodings2.append(face_encodings)
#
# compare_matches = face_recognition.compare_faces(face_encodings1,face_encodings2)
#
# print(compare_matches)

import cv2
import face_recognition

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()

    face_locations = face_recognition.face_locations(frame)
    for index, (x, y, w, h) in enumerate(face_locations):
        x *= 4
        y *= 4
        w *= 4
        h *= 4
        faces = frame[x:w, h:y]
        # cv2.imwrite('Faces_in/face_in_' + str(index) + '.jpg', faces)
        cv2.rectangle(frame, (h, x), (y, w), (0, 0, 255), 2)
    cv2.imshow("WebCam", frame)
    cv2.waitKey(0)
cap.release()
cv2.closeAllWindows()