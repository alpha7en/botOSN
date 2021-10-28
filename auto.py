# -*- coding: utf8 -*-
"""
!!!!!!!!!!!!!!!
ВЕСА ВЗЯЛ ТУТ!
https://pjreddie.com/media/files/yolov3.weights
НА РЕПЕ ИХ НЕТУ!
весят они 250мб, так что считай объём сервера
!!!!!!!!!!!!!!!!
!!!!!!!!!!!!!!!!
!!!!!!!!!!!!!!!!

"""
import cv2
import numpy as np
import time
import sys
import os

CONFIDENCE = 0.6
SCORE_THRESHOLD = 0.5
IOU_THRESHOLD = 0.5

# конфигурация нейронной сети
config_path = "auto_data/cfg/yolov3.cfg"
# файл весов сети YOLO
weights_path = "auto_data/weights/yolov3.weights"
# weights_path = "weights/yolov3-tiny.weights"

# загрузка всех меток классов (объектов)
labels = ['человек', 'велосипед', 'автомобиль', 'мотоцикл', 'самолет', 'автобус', 'поезд', 'грузовик', 'лодка',
          'светофор', 'пожарный гидрант', 'знак остановки', 'парковочный счетчик', 'скамейка', 'птица', 'кошка',
          'собака', 'лошадь', 'овца', 'корова', 'слон', 'медведь', 'зебра', 'жираф', 'рюкзак', 'зонтик', 'сумка',
          'галстук', 'чемодан', 'фрисби', 'лыжи', 'сноуборд', 'спортивный мяч', 'воздушный змей', 'бейсбольная бита',
          'бейсбольная перчатка', 'скейтборд', 'доска для серфинга', 'теннисная ракетка', 'бутылка', 'бокал',
          'для вина чашка', 'вилка', 'нож', 'ложка', 'чаша', 'банан', 'яблоко', 'сэндвич', 'апельсин', 'брокколи',
          'морковка', 'хот-дог', 'пицца', 'пончик', 'торт', 'стул', 'диван', 'растение в горшке', 'кровать',
          'обеденный стол', 'туалет', 'телевизор монитор', 'ноутбук', 'мышь', 'пульт',
          'дистанционного управления клавиатура', 'сотовый телефон', 'микроволновая', 'печь', 'тостер', 'раковина',
          'холодильник', 'книга', 'часы', 'ваза', 'ножницы', 'плюшевый мишка', 'фен', 'зубная щетк']
# генерируем цвета для каждого объекта и последующего построения

# загружаем сеть YOLO
net = cv2.dnn.readNetFromDarknet(config_path, weights_path)

path_name = "auto_data/images/food.jpg"
image = cv2.imread(path_name)
file_name = os.path.basename(path_name)
filename, ext = file_name.split(".")

h, w = image.shape[:2]
# создать 4D blob
blob = cv2.dnn.blobFromImage(image, 1 / 255.0, (416, 416), swapRB=True, crop=False)

# устанавливает blob как вход сети
net.setInput(blob)
# получаем имена всех слоев
ln = net.getLayerNames()

ln = [ln[i - 1] for i in net.getUnconnectedOutLayers()]
# прямая связь (вывод) и получение выхода сети
# измерение времени для обработки в секундах
start = time.perf_counter()
layer_outputs = net.forward(ln)
time_took = time.perf_counter() - start
print(f"Потребовалось: {time_took:.2f}s")

font_scale = 1
thickness = 1
boxes, confidences, class_ids = [], [], []
# перебираем каждый из выходов слоя
for output in layer_outputs:
    # перебираем каждое обнаружение объекта
    for detection in output:
        # извлекаем идентификатор класса (метку) и достоверность (как вероятность)
        # обнаружение текущего объекта
        scores = detection[5:]
        class_id = np.argmax(scores)
        confidence = scores[class_id]
        # отбросьте слабые прогнозы, убедившись, что обнаруженные
        # вероятность больше минимальной вероятности
        if confidence > CONFIDENCE:
            # масштабируем координаты ограничивающего прямоугольника относительно
            # размер изображения, учитывая, что YOLO на самом деле
            # возвращает центральные координаты (x, y) ограничивающего
            # поля, за которым следуют ширина и высота поля
            box = detection[:4] * np.array([w, h, w, h])
            (centerX, centerY, width, height) = box.astype("int")
            # используем центральные координаты (x, y) для получения вершины и
            # и левый угол ограничительной рамки
            x = int(centerX - (width / 2))
            y = int(centerY - (height / 2))
            # обновить наш список координат ограничивающего прямоугольника, достоверности,
            # и идентификаторы класса
            boxes.append([x, y, int(width), int(height)])
            confidences.append(float(confidence))
            class_ids.append(class_id)

# перебираем сохраняемые индексы
r = []
for i in range(len(boxes)):
    r.append([confidences[i], float(i)])

print(r)
res = np.array(r)
otvet = np.sort(res, axis=0)
print(otvet)
# text = f"{labels[class_ids[i]]}: {confidences[i]:.2f}"
#     print(text)
