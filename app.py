from flask import Flask, render_template, Response,url_for, redirect, request
from camera import VideoCamera
import cv2
import time

app = Flask(__name__)

@app.route("/")
def home():
    # rendering web page
    return render_template('index.html')

def gen(camera):
    while True:
        # get camera frame
        frame = camera.face_eyes_detect()
        yield(b'--frame\r\n'
                  b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

@app.route("/video_feed")
def video_feed():
    return Response(gen(VideoCamera()),
          mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    # defining server ip address and port
    app.run(debug=False)
