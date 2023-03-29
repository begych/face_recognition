# import cv2
# import face_recognition
#
#
# cap = cv2.VideoCapture(0)
#
# process_this_frame = True
# face_locations = []
#
# while True:
#     ret, img = cap.read()
#     if process_this_frame:
#         # small_img = cv2.resize(img, (0, 0), fx = 0.25, fy = 0.25)
#         face_locations = face_recognition.face_locations(img)
#     process_this_frame = not process_this_frame
#     # print(face_locations)
#
#     for index, (x, y, w, h) in enumerate(face_locations):
#         # x *= 4
#         # y *= 4
#         # w *= 4
#         # h *= 4
#         faces = img
#         cv2.imwrite('Faces/face'+str(index)+'.jpg', faces)
#         cv2.rectangle(img, (h, x), (y, w), (0, 0, 255), 2)
#
#
#
#
#     cv2.imshow("Camera", img)
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break
#
# cap.release()
# cv2.destroyAllWindows()

import cv2
import face_recognition
# import subprocess
# import runpy
# os.system("/home/asus/PycharmProjects/FaceDetect/Comparefaces.py")
# subprocess.Popen('/home/asus/PycharmProjects/FaceDetect/Comparefaces.py')
# runpy.run_path(path_name='/home/asus/PycharmProjects/FaceDetect/Comparefaces.py')

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
            cv2.imwrite('Faces_in/face_in_' + str(index) + '.jpg', faces)
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
            cv2.imwrite('Faces_out/face_out_' + str(index) + '.jpg', faces)
            cv2.rectangle(img1, (h, x), (y, w), (0, 0, 255), 2)
        cv2.imshow('Cam 1', img1)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


cap_0.release()
cap_1.release()
cv2.destroyAllWindows()