# import cv2
# import face_recognition
# import pickle5 as pickle
# import os
# import shutil
#
#
# with open("Data/data.pickle", "rb") as f:
#     data = pickle.load(f)
# print(data)
#
# while True:
#     try:
#         if len(os.listdir("Faces_in")) != 0:
#             lenlist = len(os.listdir("Faces_in"))
#             print('#' * 20)
#
#             for index in range(len(os.listdir("Faces_in"))):
#                 shutil.move("Faces_in/"+str(os.listdir('Faces_in')[0]),"FacesDir_in/"+str(os.listdir('Faces_in')[0]))
#
#             print("Face to FaceDir")
#
#             for unknown_face_index in range(len(os.listdir("FacesDir_in"))):
#
#                 unknown_face = cv2.imread("FacesDir_in/"+str(os.listdir("FacesDir_in")[unknown_face_index]))
#                 unknown_face_locations = face_recognition.face_locations(unknown_face)
#                 unknown_face_encodings = face_recognition.face_encodings(unknown_face,unknown_face_locations)
#
#                 for known_face_index in range(len(os.listdir("KnownFaces"))):
#
#                     known_face = cv2.imread("KnownFaces/"+str(os.listdir("KnownFaces")[known_face_index]))
#                     known_face_locations = face_recognition.face_locations(known_face)
#                     known_face_encodings = face_recognition.face_encodings(known_face, known_face_locations)[0]
#                     compare_matches = face_recognition.compare_faces(known_face_encodings,unknown_face_encodings)
#
#
#                     if True in compare_matches :
#                         print(unknown_face_index,' ',os.listdir('FacesDir_in')[unknown_face_index],' -- ',
#                               known_face_index,' ',os.listdir("KnownFaces")[known_face_index])
#
#
#                         shutil.move("FacesDir_in/"+str(os.listdir('FacesDir_in')[unknown_face_index]),
#                                     "DetectedFaces/"+str(os.listdir('FacesDir_in')[unknown_face_index]))
#
#                         break
#
#             print("compare end")
#
#             if len(os.listdir("FacesDir_in")) != 0 :
#                 for unknown_face_index in range(len(os.listdir("Faces_in"))):
#                     shutil.move("FacesDir_in/"+str(os.listdir('FacesDir_in')[0]),
#                                 "UnknownFaces/"+str(os.listdir('FacesDir_in')[0]))
#
#             print("-|" * 20)
#     except:
#         continue

import cv2
import face_recognition
import pickle5 as pickle
import os
import shutil

with open("Data/database.pickle", "rb") as f:
    database = pickle.load(f)


while True:
    try:
        if len(os.listdir("Faces_in")) != 0:
            lenlist = len(os.listdir("Faces_in"))
            print('#' * 20)

            for index in range(len(os.listdir("Faces_in"))):
                shutil.move("Faces_in/"+str(os.listdir('Faces_in')[0]),"FacesDir_in/"+str(os.listdir('Faces_in')[0]))

            print("Faces_in to FacesDir_in")

            for unknown_face_index in range(len(os.listdir("FacesDir_in"))):

                print(os.listdir("FacesDir_in")[unknown_face_index])

                unknown_face = cv2.imread("FacesDir_in/"+str(os.listdir("FacesDir_in")[unknown_face_index]))
                unknown_face_locations = face_recognition.face_locations(unknown_face)
                unknown_face_encodings = face_recognition.face_encodings(unknown_face, unknown_face_locations)[0]
                # face_recognition.compare_faces()


                for index in range(len(database)):
                    data = database[index]
                    known_face_encodings = data['encodings']
                    # print("known -- ",known_face_encodings)

                    compare_matches = face_recognition.compare_faces(known_face_encodings, unknown_face_encodings)

                    print(compare_matches)

                    k = 0
                    for i in range(len(compare_matches)):
                        if True in compare_matches[i]  :
                            k += 1

                    if k >= 3 :
                        print("Face_Detected")
                        shutil.move("FacesDir_in/" + str(os.listdir('FacesDir_in')[unknown_face_index]),
                                    "DetectedFaces/" + str(os.listdir('FacesDir_in')[unknown_face_index]))



            if len(os.listdir("FacesDir_in")) != 0:
                for unknown_face_index in range(len(os.listdir("Faces_in"))):
                    shutil.move("FacesDir_in/" + str(os.listdir('FacesDir_in')[0]),
                                "UnknownFaces/" + str(os.listdir('FacesDir_in')[0]))

            print("+++" * 20)
    except:
        continue