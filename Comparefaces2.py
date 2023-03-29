import cv2
import face_recognition
import os
import shutil
import pymysql
from config import host, user, password, db_name


while True:
    try:
        if len(os.listdir("Faces_out")) != 0:
            lenlist = len(os.listdir("Faces_out"))
            print('#' * 20)

            for index in range(len(os.listdir("Faces_out"))):
                shutil.move("Faces_out/"+str(os.listdir('Faces_out')[0]),"FacesDir_out/"+str(os.listdir('Faces_out')[0]))

            print("Face to FaceDir")

            for unknown_face_index in range(len(os.listdir("FacesDir_out"))):

                unknown_face = cv2.imread("FacesDir_out/"+str(os.listdir("FacesDir_out")[unknown_face_index]))
                unknown_face_locations = face_recognition.face_locations(unknown_face)
                unknown_face_encodings = face_recognition.face_encodings(unknown_face,unknown_face_locations)

                for known_face_index in range(len(os.listdir("KnownFaces"))):

                    known_face = cv2.imread("KnownFaces/"+str(os.listdir("KnownFaces")[known_face_index]))
                    known_face_locations = face_recognition.face_locations(known_face)
                    known_face_encodings = face_recognition.face_encodings(known_face, known_face_locations)[0]
                    compare_matches = face_recognition.compare_faces(known_face_encodings,unknown_face_encodings)


                    if True in compare_matches :
                        print(unknown_face_index,' ',os.listdir('FacesDir_out')[unknown_face_index],' -- ',
                              known_face_index,' ',os.listdir("KnownFaces")[known_face_index])

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
                                    cursor.execute(update_query,val)
                                    connection.commit()

                            finally:
                                connection.close()

                        except Exception as ex:
                            print("connection refused...")
                            print(ex)


                        shutil.move("FacesDir_out/"+str(os.listdir('FacesDir_out')[unknown_face_index]),
                                    "DetectedFaces/"+str(os.listdir('FacesDir_out')[unknown_face_index]))

                        break

            print("compare end")

            if len(os.listdir("FacesDir_out")) != 0 :
                for unknown_face_index in range(len(os.listdir("Faces_out"))):
                    shutil.move("FacesDir_out/"+str(os.listdir('FacesDir_out')[0]),
                                "UnknownFaces/"+str(os.listdir('FacesDir_out')[0]))

            print("-|" * 20)
    except:
        continue