#!/usr/bin/env python
from flask import Flask, render_template, Response
import cv2 as cv
import time

app = Flask(__name__)

vc = cv.VideoCapture(0)


def gen():
    if vc.isOpened(): # try to get the first frame
        print("capturing frames")
        rval, frame = vc.read()
    else:
        rval = False
    while rval:
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n'
               b'\r\n' + frame + b'\r\n')
        time.sleep(0.04) # my Firefox needs some time to display image / Chrome displays image without it 
                         # 0.04s = 40ms = 25 frames per second

@app.route('/')
def index():
    return 'image:<br><img src="/video">'
    #return render_template_string('image:<br><img src="{{ url_for("video") }}">')

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)