#!/usr/bin/env python
from flask import Flask, render_template, Response
import cv2 as cv

app = Flask(__name__)

vc = cv.VideoCapture(0)

@app.route('/')
def index():
    return render_template('index.html')

def gen():
    if vc.isOpened(): # try to get the first frame
        print("capturing frames")
        rval, frame = vc.read()
    else:
        rval = False
    while rval:
        return Response(gen(), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/')
def index():
    return 'image:<br><img src="/video">'
    #return render_template_string('image:<br><img src="{{ url_for("video") }}">')

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)