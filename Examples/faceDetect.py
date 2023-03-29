import cv2

# Импортировали модуль opencv


img = cv2.imread("Resources/FaceToDetect.jpg")
img = cv2.resize(img, (300, 500))
# Методом imread мы как бы читаем наше фото, после этого можем производить манипуляции над ним
face_recog = cv2.CascadeClassifier('/home/begych/PycharmProjects/pythonProject/venv/lib/python3.8/site-packages/cv2/data/haarcascade_frontalface_default.xml')
# Методом CascadeClassifier мы подключаем уже натренированную нейронную модель.

face_result = face_recog.detectMultiScale(img, scaleFactor=2, minNeighbors=3)
# Метод detectMultiScale выполняет поиск лица на фото которые мы указали в качестве первого аргумента
# Аргумент scaleFactor это как бы шаг масштабирования (насколько большое лицо)
# Аргумент minNeighbors это что то вроде указания о том, сколько лиц может быть рядом
# Значение этим аргументам я взял с воздуха, но все же это работает
# Вы можете поиграться с ними, главное не ставьте scaleFactor=1 так как будет ошибка
# print( face_result )

if len(face_result) != 0:
    # Функция, выполнение которой мы записали в face_result (detectMultiScale), возвращает список, если он пуст, значит лиц на фото нет

    for index, (x, y, w, h) in enumerate(face_result):
        # Мы проходимся по всем элементам списка, и получаем позицию x,y и ширину с высотой(w,h)
        img = img[x:y + h]
        # Тут думаю все понятно, мы обрезаем картинку (она у нас как список с цветами) с точки x до точки y+h

        cv2.imwrite('Resources/Result.jpg', img)
# Этот метод записывает получившуюся картинку по опр. пути, принимает путь и само изображение
cv2.imshow("Result", img)
# Этот метод выводит результат на экран. Первый аргумент - что то по типу комментария к картинке, второй - сама картинка
cv2.waitKey(0)
# От этого, зависит какое кол-во времени наша картинка будет отображаться на экране. Если передаем 0 то будет отображаться пока не закроем(бесконечно)ся
