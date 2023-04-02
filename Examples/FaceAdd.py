import cv2
import face_recognition
import pymysql
from config import host, user, password, db_name

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
            lastID = cursor.execute("SELECT last_insert_id() FROM Face_django.face_person;")

    finally:
        connection.close()

except Exception as ex:
    print("connection refused...")
    print(ex)


lastID += 1

cap = cv2.VideoCapture(0)
cap.set(3, 500)
cap.set(4, 500)

while True:
    ret, img = cap.read()
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    face_locations = face_recognition.face_locations(img_gray)
    for index, (x, y, w, h) in enumerate(face_locations):
        cv2.imwrite('KnownFaces/' + str(lastID) + '.jpg', img)

        cv2.rectangle(img, (h, x), (y, w), (0, 0, 255), 2)

    cv2.imshow("Camera", img)
    # key = cv2.waitKey(20)
    # if key == 27:  # exit on ESC
    #     break
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    # cv2.waitKey(1)
cap.release()
cv2.destroyAllWindows()