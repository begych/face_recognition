import os
import cv2
import pickle5 as pickle
import face_recognition

with open("Data/database.pickle", "rb") as f:
    database = pickle.load(f)

data = database[0]
known_face_encodings = data["encodings"]


img1 = cv2.imread("Faces_in/face_in_0.jpg")
img2 = cv2.imread("Faces_in/face_in_1.jpg")

# face_locations1 = face_recognition.face_locations(img1)
# face_encodings1 = face_recognition.face_encodings(img1,face_locations1)
# face_encodings = [face_encodings1]

face_locations2 = face_recognition.face_locations(img2)
face_encodings2 = face_recognition.face_encodings(img2, face_locations2)
# face_encodings2.append(face_encodings)

compare_matches = face_recognition.compare_faces(known_face_encodings,face_encodings2)

print(compare_matches)