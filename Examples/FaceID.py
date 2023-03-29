import cv2
import face_recognition
import os

# Импортируем все модули

cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)
# Методом VideoCapture мы получаем видео, тут можно указать путь к mp4 файлу и прочитать его
# Указав 0 мы получаем видео с ВЕБ КАМЕРЫ

image_to_recognition = face_recognition.load_image_file('Resources/Result.jpg')
# Теперь начинаем работать с face_recognition, метод load_image_file получает изображение
# В данном случае то фото рами малека которые мы обрезали второй программой

image_enc = face_recognition.face_encodings(image_to_recognition)[0]
# Тут методом face_encodings мы получаем КОДИРОВКУ ЛИЦА рами малека.
# Просто у каждого фото с лицом (да и не только) есть КОДИРОВКА.
# Если у нас есть 2 фото с лицами и если их кодировки совпадают, значит на фото один и тот же человвек
print(image_enc)
recognizer_cc = cv2.CascadeClassifier('/home/begych/PycharmProjects/pythonProject/venv/lib/python3.8/site-packages/cv2/data/haarcascade_frontalface_default.xml')
# Про это уже говорил

# Любое видео, это быстро меняющиеся картинки, от того и создается эффект анимации
# Здесь тот же принцип, в бесконечном цикле мы очень быстро меняем изображения и получаем видео
while True:
    success, img = cap.read()
    # Получаем изображение которое будем быстро показывать, если изображение не получено success будет равен False

    recognize = recognizer_cc.detectMultiScale(img, scaleFactor=2, minNeighbors=3)
    # Про это уже говорил
    cv2.imshow("Camera", img)
    if len(recognize) != 0:
        # Если на фото есть лицо, делаем то, что ниже
        unknown_face = face_recognition.face_encodings(img)
        # Получем кодировку неизвестного лица (лица которое на видео)

        compare = face_recognition.compare_faces(unknown_face, image_enc)
        print(compare)
        # Сравниваем две кодировки (кодировку рами малека и кодировку неизвестного лица)
        # Первый параметр надо передать как список (за это и обернули в [])
        # Второй это кодировка рами малека (этот аргумент передаем просто)

        if True in compare:
            # Если мы зашли сюда, значит лица одинаковые
            print('Лицо распознано')
        else:
            print('НЕ распознано')
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break