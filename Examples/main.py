# import cv2
#
# img = cv2.imread("Resources/image.jpg")
#
# cv2.imshow("Picture", img)
# cv2.waitKey(0)

# import cv2
#
# cap = cv2.VideoCapture("Resources/test_video.mp4")
#
# while True:
#     success, img = cap.read()
#     cv2.imshow("Video", img)
#     if cv2.waitKey(1) & 0xFF == ord("q"):
#         break
#
# import cv2
#
# cap = cv2.VideoCapture(0)
#
# cap.set(3, 500)
# cap.set(4, 500)
#
# while True:
#     success, img = cap.read()
#     cv2.imshow("Camera", img)
#     if cv2.waitKey(1) & 0xFF == ord("q"):
#         break

# import cv2
# import face_recognition
#
# image = face_recognition.load_image_file("Resources/FaceToDetect.jpg")
# image = image[:, :, ::-1]
# image = cv2.resize(image, (480, 640))
# cv2.imshow("surat", image)
# cv2.waitKey(0)


# import yaml
# import numpy as np
# a = []
# b = []
# i,j = 0,0
# for i in range(10):
#     for j in range(10):
#         b += [j]
#     a += [b]
#     b = []
#     with open('primer.yml','w') as f:
#         yaml.dump(a, f)
# with open('primer.yml','r') as f:
#     a = yaml.safe_load(f)
# print(a)

# import face_recognition
# import cv2
# import json
#
# a = []
#
# img = cv2.imread('Resources/hasbik.jpg')
# img = cv2.resize(img, (500, 500))
# # gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#
# face_locations = face_recognition.face_locations(img)
# face_encoding = face_recognition.face_encodings(img,face_locations)[0]
#
#
# with open('primer.json','w') as f:
#     json.dump(face_encoding,f)

# with open('primer.yml', 'r') as f:
#     a += yaml.safe_load_all(f)
# print(a)
# print(face_encoding)


# cv2.imshow('Surat', img)
# cv2.waitKey(0)

# import cv2
# import face_recognition
#
# cap = cv2.VideoCapture(0)
#
# while True:
#     ret, img = cap.read()
#     cv2.imshow("camera", img)
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break
# cap.realese()
# cv2.destroyAllWindows()

# import cv2
# import threading
#
# class camThread(threading.Thread):
#     def __init__(self, previewName, camID):
#         threading.Thread.__init__(self)
#         self.previewName = previewName
#         self.camID = camID
#     def run(self):
#         print("Starting " + self.previewName)
#         camPreview(self.previewName, self.camID)
# def camPreview(previewName, camID):
#     cv2.namedWindow(previewName)
#     cam = cv2.VideoCapture(camID)
#     if cam.isOpened():
#         rval, frame = cam.read()
#     else:
#         rval = False
#     while rval:
#         cv2.imshow(previewName, frame)
#         rval, frame = cam.read()
#         key = cv2.waitKey(20)
#         if key == 27:  # exit on ESC
#             break
#     cv2.destroyWindow(previewName)
# # Create threads as follows
# thread1 = camThread("Camera 1", 0)
# thread2 = camThread("Camera 2", 2)
# # thread3 = camThread("Camera 3", 2)
# thread1.start()
# thread2.start()
# # thread3.start()
# print()
# print("Active threads", threading.activeCount())

import numpy as np
import cv2
import face_recognition

cap_0 = cv2.VideoCapture(0)
cap_1 = cv2.VideoCapture(2)

process_this_frame = True
face_locations0 = []
face_locations1 = []

while True:
    # Capture frame-by-frame
    ret0, img0 = cap_0.read()
    ret1, img1 = cap_1.read()

    if (ret0):
        # if process_this_frame:
        small_img0 = cv2.resize(img0, (0, 0), fx = 0.25, fy = 0.25)
        face_locations0 = face_recognition.face_locations(small_img0)
        # process_this_frame = not process_this_frame
        # print(face_locations)

        for index, (x, y, w, h) in enumerate(face_locations0):
            x *= 4
            y *= 4
            w *= 4
            h *= 4
            faces = img0
            # cv2.imwrite('Faces/face' + str(index) + '.jpg', faces)
            cv2.rectangle(img0, (h, x), (y, w), (0, 0, 255), 2)
        cv2.imshow('Cam 0', img0)



    if (ret1):
        # if process_this_frame:
        small_img1 = cv2.resize(img1, (0, 0), fx = 0.25, fy = 0.25)
        face_locations1 = face_recognition.face_locations(small_img1)
        # process_this_frame = not process_this_frame
        # print(face_locations)

        for index, (x, y, w, h) in enumerate(face_locations1):
            x *= 4
            y *= 4
            w *= 4
            h *= 4
            faces = img1
            # cv2.imwrite('Faces/face' + str(index) + '.jpg', faces)
            cv2.rectangle(img1, (h, x), (y, w), (0, 0, 255), 2)
        cv2.imshow('Cam 1', img1)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything is done, release the capture
cap_0.release()
cap_1.release()
cv2.destroyAllWindows()