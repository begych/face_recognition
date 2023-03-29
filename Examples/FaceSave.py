import cv2
import face_recognition
import numpy as np
import json
from json import JSONEncoder
from datetime import datetime

class NumpyArrayEncoder(JSONEncoder):
    def default(self, obj):
        if isinstance(obj, np.ndarray):
            return obj.tolist()
        return JSONEncoder.default(self, obj)

class DateTimeEncoder(JSONEncoder):
    def default(self, o):
        if isinstance(o, datetime):
            return o.isoformat()
        return JSONEncoder.default(self, o)

i = 0
DateTimeData = {}
FaceEncsData = {}
with open('sample.json', 'r') as f:
    hasb_arr = json.load(f)
known_face_encodings = [np.asarray(hasb_arr)]

cap = cv2.VideoCapture(2)
cap.set(3, 480)
cap.set(4, 640)

process_this_frame = True

while True :
    ret, img = cap.read()
    if process_this_frame:
        small_img = cv2.resize(img, (0, 0), fx=0.25, fy=0.25)

        unknown_face_loc = face_recognition.face_locations(small_img)
        unknown_face_encs = face_recognition.face_encodings(small_img, unknown_face_loc)

        for unknown_face_enc in unknown_face_encs:
            unknown_face_compares = face_recognition.compare_faces(known_face_encodings, unknown_face_enc)

            print(unknown_face_compares)

            if unknown_face_compares[len(unknown_face_compares)-1] == False :
                i += 1

                DateTimeData[i] = datetime.now()

                known_face_encodings += [unknown_face_enc]
                FaceEncsData[i] = [unknown_face_enc]

                with open('dFace.json', 'w') as f:
                    json.dump(FaceEncsData, f, cls = NumpyArrayEncoder)

                with open('dTime.json', 'w') as f:
                    json.dump(DateTimeData, f, cls = DateTimeEncoder)


    process_this_frame = not (process_this_frame)


    cv2.imshow("Camera", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


cap.release()
cv2.destroyAllWindows()