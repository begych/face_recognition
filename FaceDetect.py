import cv2
import face_recognition
import pymysql
from config import host, user, password, db_name
import os
import shutil


class FaceRecognition:
    def FaceAdd(self):
        try:
            connection = pymysql.connect(
                host=host,
                port=3306,
                user=user,
                password=password,
                database=db_name,
                cursorclass=pymysql.cursors.DictCursor
            )

            try:
                with connection.cursor() as cursor:
                    lastID = cursor.execute("SELECT last_insert_id() FROM FaceData.users;")

            finally:
                connection.close()

        except Exception as ex:
            print("connection refused...")
            print(ex)

        lastID += 1

        cap = cv2.VideoCapture(0)
        cap.set(3, )
        cap.set(4, 500)

        while True:
            ret, img = cap.read()
            img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            face_locations = face_recognition.face_locations(img_gray)
            for index, (x, y, w, h) in enumerate(face_locations):
                cv2.imwrite('KnownFaces/' + str(lastID) + '.jpg', img)

                cv2.rectangle(img, (h, x), (y, w), (0, 0, 255), 2)

            cv2.imshow("Camera", img)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        cap.release()
        cv2.destroyAllWindows()

    def FaceScreen(self):
        cap_0 = cv2.VideoCapture(0)
        cap_1 = cv2.VideoCapture(2)

        # process_this_frame = True
        face_locations0 = []
        face_locations1 = []

        while True:
            # Capture frame-by-frame
            ret0, img0 = cap_0.read()
            ret1, img1 = cap_1.read()

            if (ret0):
                # if process_this_frame:
                small_img0 = cv2.resize(img0, (0, 0), fx=0.25, fy=0.25)
                face_locations0 = face_recognition.face_locations(small_img0)
                # process_this_frame = not process_this_frame
                # print(face_locations)

                for index, (x, y, w, h) in enumerate(face_locations0):
                    x *= 4
                    y *= 4
                    w *= 4
                    h *= 4
                    faces = img0
                    cv2.imwrite('Faces_in/face_in_' + str(index) + '.jpg', faces)
                    cv2.rectangle(img0, (h, x), (y, w), (0, 0, 255), 2)
                cv2.imshow('Cam 0', img0)

            if (ret1):
                # if process_this_frame:
                small_img1 = cv2.resize(img1, (0, 0), fx=0.25, fy=0.25)
                face_locations1 = face_recognition.face_locations(small_img1)
                # process_this_frame = not process_this_frame
                # print(face_locations)

                for index, (x, y, w, h) in enumerate(face_locations1):
                    x *= 4
                    y *= 4
                    w *= 4
                    h *= 4
                    faces = img1
                    cv2.imwrite('Faces_out/face_out_' + str(index) + '.jpg', faces)
                    cv2.rectangle(img1, (h, x), (y, w), (0, 0, 255), 2)
                cv2.imshow('Cam 1', img1)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        cap_0.release()
        cap_1.release()
        cv2.destroyAllWindows()

    def Comparefaces(self):
        while True:
            try:
                if len(os.listdir("Faces_in")) != 0:
                    lenlist = len(os.listdir("Faces_in"))
                    print('#' * 20)

                    for index in range(len(os.listdir("Faces_in"))):
                        shutil.move("Faces_in/" + str(os.listdir('Faces_in')[0]),
                                    "FacesDir_in/" + str(os.listdir('Faces_in')[0]))

                    print("Face to FaceDir")

                    for unknown_face_index in range(len(os.listdir("FacesDir_in"))):

                        unknown_face = cv2.imread("FacesDir_in/" + str(os.listdir("FacesDir_in")[unknown_face_index]))
                        unknown_face_locations = face_recognition.face_locations(unknown_face)
                        unknown_face_encodings = face_recognition.face_encodings(unknown_face, unknown_face_locations)

                        for known_face_index in range(len(os.listdir("KnownFaces"))):

                            known_face = cv2.imread("KnownFaces/" + str(os.listdir("KnownFaces")[known_face_index]))
                            known_face_locations = face_recognition.face_locations(known_face)
                            known_face_encodings = face_recognition.face_encodings(known_face, known_face_locations)[0]
                            compare_matches = face_recognition.compare_faces(known_face_encodings,
                                                                             unknown_face_encodings)

                            if True in compare_matches:
                                print(unknown_face_index, ' ', os.listdir('FacesDir_in')[unknown_face_index], ' -- ',
                                      known_face_index, ' ', os.listdir("KnownFaces")[known_face_index])

                                try:
                                    inttostr = str(known_face_index)
                                    connection = pymysql.connect(
                                        host=host,
                                        port=3306,
                                        user=user,
                                        password=password,
                                        database=db_name,
                                        cursorclass=pymysql.cursors.DictCursor

                                    )
                                    try:
                                        inttostr = str(known_face_index)
                                        with connection.cursor() as cursor:
                                            # formatted_datetime = datetime.now()
                                            update_query = "UPDATE `users` SET  " \
                                                           "time_of_arrival = current_timestamp() WHERE id = %s;"
                                            val = (str(os.listdir("KnownFaces")[known_face_index])[:-4])
                                            cursor.execute(update_query, val)
                                            connection.commit()

                                    finally:
                                        connection.close()

                                except Exception as ex:
                                    print("connection refused...")
                                    print(ex)

                                shutil.move("FacesDir_in/" + str(os.listdir('FacesDir_in')[unknown_face_index]),
                                            "DetectedFaces/" + str(os.listdir('FacesDir_in')[unknown_face_index]))

                                break

                    print("compare end")

                    if len(os.listdir("FacesDir_in")) != 0:
                        for unknown_face_index in range(len(os.listdir("Faces_in"))):
                            shutil.move("FacesDir_in/" + str(os.listdir('FacesDir_in')[0]),
                                        "UnknownFaces/" + str(os.listdir('FacesDir_in')[0]))

                    print("-|" * 20)
            except:
                continue

    def Comparefaces2(self):
        while True:
            try:
                if len(os.listdir("Faces_out")) != 0:
                    lenlist = len(os.listdir("Faces_out"))
                    print('#' * 20)

                    for index in range(len(os.listdir("Faces_out"))):
                        shutil.move("Faces_out/" + str(os.listdir('Faces_out')[0]),
                                    "FacesDir_out/" + str(os.listdir('Faces_out')[0]))

                    print("Face to FaceDir")

                    for unknown_face_index in range(len(os.listdir("FacesDir_out"))):

                        unknown_face = cv2.imread("FacesDir_out/" + str(os.listdir("FacesDir_out")[unknown_face_index]))
                        unknown_face_locations = face_recognition.face_locations(unknown_face)
                        unknown_face_encodings = face_recognition.face_encodings(unknown_face, unknown_face_locations)

                        for known_face_index in range(len(os.listdir("KnownFaces"))):

                            known_face = cv2.imread("KnownFaces/" + str(os.listdir("KnownFaces")[known_face_index]))
                            known_face_locations = face_recognition.face_locations(known_face)
                            known_face_encodings = face_recognition.face_encodings(known_face, known_face_locations)[0]
                            compare_matches = face_recognition.compare_faces(known_face_encodings,
                                                                             unknown_face_encodings)

                            if True in compare_matches:
                                print(unknown_face_index, ' ', os.listdir('FacesDir_out')[unknown_face_index], ' -- ',
                                      known_face_index, ' ', os.listdir("KnownFaces")[known_face_index])

                                try:
                                    inttostr = str(known_face_index)
                                    connection = pymysql.connect(
                                        host=host,
                                        port=3306,
                                        user=user,
                                        password=password,
                                        database=db_name,
                                        cursorclass=pymysql.cursors.DictCursor

                                    )
                                    try:
                                        inttostr = str(known_face_index)
                                        with connection.cursor() as cursor:
                                            # formatted_datetime = datetime.now()
                                            update_query = "UPDATE `users` SET  " \
                                                           "departure_time = current_timestamp() WHERE id = %s;"
                                            val = (str(os.listdir("KnownFaces")[known_face_index])[:-4])
                                            cursor.execute(update_query, val)
                                            connection.commit()

                                    finally:
                                        connection.close()

                                except Exception as ex:
                                    print("connection refused...")
                                    print(ex)

                                shutil.move("FacesDir_out/" + str(os.listdir('FacesDir_out')[unknown_face_index]),
                                            "DetectedFaces/" + str(os.listdir('FacesDir_out')[unknown_face_index]))

                                break

                    print("compare end")

                    if len(os.listdir("FacesDir_out")) != 0:
                        for unknown_face_index in range(len(os.listdir("Faces_out"))):
                            shutil.move("FacesDir_out/" + str(os.listdir('FacesDir_out')[0]),
                                        "UnknownFaces/" + str(os.listdir('FacesDir_out')[0]))

                    print("-|" * 20)
            except:
                continue