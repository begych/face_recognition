# import json
#
# # Data to be written
# dictionary = {
#     "name": "sathiyajith",
#     "rollno": 56,
#     "cgpa": 8.6,
#     "phonenumber": "9976770500"
# }
#
# # Serializing json
# json_object = json.dumps(dictionary, indent=4)
#
# # Writing to sample.json
# with open("sample.json", "w") as outfile:
#     outfile.write(json_object)


# import json
#
# # Opening JSON file
# with open('sample.json', 'r') as openfile:
#     # Reading from json file
#     json_object = json.load(openfile)
#
# print(json_object)
# print(type(json_object))

import cv2
import face_recognition
import json
from json import JSONEncoder
import numpy as np
from datetime import datetime

# img = cv2.imread("Resources/FaceToDetect.jpg")

# face_img = face_recognition.face_locations(img)
# face_img_enc = face_recognition.face_encodings(img, face_img)[0]


hasbik = cv2.imread('Resources/hasbik.jpg')
# hasbik = cv2.resize(img, (500, 500))

face_hasbik = face_recognition.face_locations(hasbik)
face_hasbik_enc = face_recognition.face_encodings(hasbik, face_hasbik)[0]

class DateTimeEncoder(JSONEncoder):
    def default(self, o):
        if isinstance(o, datetime):
            return o.isoformat()

        return JSONEncoder.default(self, o)

class NumpyArrayEncoder(JSONEncoder):
    def default(self, obj):
        if isinstance(obj, np.ndarray):
            return obj.tolist()
        return JSONEncoder.default(self, obj)

i = 1
# numpyData = {face_hasbik_enc}
DateTimeData = {i : datetime.now().strftime('%Y-%m-%dT%H:%M:%S')}

with open('sample.json','w') as f:
    json.dump( face_hasbik_enc, f, cls=NumpyArrayEncoder)

with open('dTime.json','w') as f:
    json.dump(DateTimeData, f, cls = DateTimeEncoder)

# with open('sample.json','r') as f:
#     a = json.load(f)

# ar = np.asarray(a[str(i)])

# print(ar)

# class NpEncoder(json.JSONEncoder):
#     def default(self, obj):
#         if isinstance(obj, np.integer):
#             return int(obj)
#         if isinstance(obj, np.floating):
#             return float(obj)
#         if isinstance(obj, np.ndarray):
#             return obj.tolist()
#         return json.JSONEncoder.default(self, obj)
#
# with open('sample.json','w') as f:
#     json.dump(face_enc, f, cls = NpEncoder)

# cv2.imshow("Hasbik's face", img)
# cv2.waitKey(0)