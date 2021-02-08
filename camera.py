import cv2
import numpy as np
import scipy.ndimage
import pyzbar.pyzbar as pyzbar
from PIL import Image

# defining face detector
face_cascade = cv2.CascadeClassifier("haarcascades/haarcascade_frontalface_default.xml")
eye_cascade = cv2.CascadeClassifier('haarcascades/haarcascade_eye.xml')

class VideoCamera(object):
    def __init__(self):
        # capturing video
        self.video = cv2.VideoCapture(0)

    def __del__(self):
        # releasing camera
        self.video.release()
                
    def face_eyes_detect(self):
        ret, frame = self.video.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)
        c=0
        for (x,y,w,h) in faces:
            cv2.rectangle(frame, (x,y), (x+w,y+h), (255, 0, 0), 2)
            roi_gray = gray[y:y+h, x:x+w]
            roi_color = frame[y:y+h, x:x+w]

            eyes = eye_cascade.detectMultiScale(roi_gray)
            for (ex,ey,ew,eh) in eyes:
                cv2.rectangle(roi_color, (ex, ey), (ex+ew, ey+eh), (0, 255, 0), 2)

            while True:
                k = cv2.waitKey(1000) & 0xFF
                print("Image "+str(c)+" saved")
                file = 'C:/Users/user/dev/HelloWorld/images/'+str(c)+'.jpg'
                cv2.imwrite(file, frame)
                c += 1    

        
        # encode Opencv raw frame to jpg and display it
        ret, jpeg = cv2.imencode('.jpg', frame)
        return jpeg.tobytes()

    
