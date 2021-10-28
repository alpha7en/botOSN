import cv2.cv2 as cv2
from PIL import Image
import random
import os
def doFace(name):
    main = Image.open(name)
    face_cascade = cv2.CascadeClassifier('stalin_haarcascade_frontalface_default.xml')
    img = cv2.imread(name)

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.15, 5)
    kor = []
    for (x, y, w, h) in faces:
        kor.append((x, y, w, h))
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
        cv2.circle(img,(x+w//2, y+2*h//3),3,(0, 0, 255),5)





    for kor_id in kor:
        us1 = Image.open('stalin_usi/'+str(random.randint(1, 3))+'.png')
        us = us1.resize(((kor_id[2])//2, (kor[0][3])//6))

        x, y,w,h = kor_id
        main.paste(us, ((x+w//4), (y+8*h//12)), us)


    main.save(name)
