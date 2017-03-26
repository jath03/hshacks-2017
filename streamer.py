from flask import Flask, render_template, Response
import cv2
app = Flask(__name__)
cam = cv2.VideoCapture(0)
def gen(cam):
    while True:
        s, img = cam.read()
        
        s, jpg = cv2.imencode('.jpg', img)
        frame = jpg.tobytes()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

@app.route('/')
def video_feed():
    return Response(gen(cam),
                    mimetype='multipart/x-mixed-replace; boundary=frame')
