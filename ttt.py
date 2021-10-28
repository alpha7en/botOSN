import cv2.cv2 as cv2
from PIL import Image
import random
import math
import os
def doFace(name, koef = 1.5, k2 = 3):
    main = Image.open(name)
    eye_cascade = cv2.CascadeClassifier('ppp.xml')

    face_cascade = cv2.CascadeClassifier('stalin_haarcascade_frontalface_default.xml')
    img = cv2.imread(name)

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.2, 4)
    kor = []
    for (x, y, w, h) in faces:
        kor.append((x, y, w, h))
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
        cv2.circle(img, (x + w // 2, y + 2 * h // 3), 3, (0, 0, 255), 5)
        roi_gray = gray[y:y + h*2//3, x:x + w]
        roi_color = img[y:y + h*2//3, x:x + w]

        eyes = eye_cascade.detectMultiScale(roi_gray, koef, k2)
        e = []
        prov = []

        for ia, (exa, eya, ewa, eha) in enumerate(eyes, 0):
            for ib, (exb, eyb, ewb, ehb) in enumerate(eyes, 0):
                if ia != ib:

                    if (exa <= exb) and (exb+ewb <= exa +ewa) and (eya <= eyb) and (eyb+ehb >= eya +eha) :
                        prov.append(ia)


                    elif (exa >= exb) and (exb+ewb >= exa +ewa) and (eya >= eyb) and (eyb+ehb >= eya +eha) :
                        prov.append(ib)



        it = []
        for i, (exb, eyb, ewb, ehb) in enumerate(eyes, 0):
            if i not in prov:
                it.append((exb, eyb, ewb, ehb))
                cv2.rectangle(roi_color, (exb, eyb), (exb + ewb, eyb + ehb), (0, 255, 255), 2)


        if len(it) == 0:
            pass
        elif len(it) == 1:

            xb, yb, wb, hb = it[0]
            сenter_b_x = xb + wb // 2
            сenter_b_y = yb + hb // 2


            us1 = Image.open('ochki/' + str(random.randint(1, 1)) + '.png')

            koif = (w*0.9) / ((us1.size)[0])
            us = us1.resize((int(w), int(koif * ((us1.size)[1]))))


            main.paste(us, (x+xb,y+yb+h//5 ), us)

        else:
            if it[0][0] > it[0][1]:
                xa, ya, wa, ha = it[0]
                xb, yb, wb, hb = it[1]
            else:
                xa, ya, wa, ha = it[1]
                xb, yb, wb, hb = it[0]
            сenter_a_x = xa + wa//2
            сenter_a_y = ya + ha // 2
            сenter_b_x = xb + wb // 2
            сenter_b_y = yb + hb // 2
            alpha = (math.atan((сenter_b_y-  сenter_a_y)/(сenter_b_x-  сenter_a_x))*180)/math.pi

            us1 = Image.open('ochki/' + str(random.randint(1, 1)) + '.png')
            l= math.sqrt((xb-xa+ wa +wb)**2+(yb-ya +hb + ha)**2)*1.58
            koif = l/((us1.size)[0])
            us = us1.resize((int(l), int(koif*((us1.size)[1]))))
            us = us.rotate(-alpha, expand = True)


            main.paste(us, (int(x+5*(xb+xa)/8-us.size[0]/3-2*us.size[1]*math.cos(90+alpha)/4),(сenter_b_y+y-int(-us.size[1]*math.sin(90+alpha)//2+6*hb/8- us.size[0]*math.cos(90+alpha)/3))), us)
            #main.paste(us, ((xa + (сenter_b_x-сenter_a_x)//2),(ya + ha//2)), us)
    main.save(name)

'''
    for kor_id in kor:
        us1 = Image.open('stalin_usi/'+str(random.randint(1, 3))+'.png')
        us = us1.resize(((kor_id[2])//2, (kor[0][3])//6))

        x, y,w,h = kor_id
        main.paste(us, ((x+w//4), (y+8*h//12)), us)


    main.save(name)
'''

