import numpy as np
import cv2
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
nose_cascade = cv2.CascadeClassifier('Nariz.xml')

cap = cv2.VideoCapture(0)
mask_on = False

while True:
    ret, frame = cap.read()

    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    wajah = face_cascade.detectMultiScale(gray,1.3,5)

    #gambar kotak
    for (x,y,w,h) in wajah:
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = frame[y:y+h, x:x+w]
        if mask_on:
            cv2.rectangle(frame,(x,y),(x+w, y+h),(0,255,0),3)
        else:
            cv2.rectangle(frame, (x,y), (x+w, y+h), (0,0,255),3)


        roi_gray = gray[y:y+h, x:x+w]
        roi_color = frame[y:y+h, x:x+w]
        hidung = nose_cascade.detectMultiScale(roi_gray,1.18,35)
        for (sx,sy,sw,sh) in hidung:
            cv2.rectangle(roi_color,(sh,sy),(sx+sw,sy+sh),(0,0,255),2)

            if len(hidung)>0:
                mask_on= False
            else:
                mask_on= True

        
    cv2.imshow('Video', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

