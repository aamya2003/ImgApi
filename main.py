import os, random
from flask import Flask, send_file

randomImgApi = Flask(__name__)

# ['img1.jpg', 'img2.jpg', 'img3.j']


@randomImgApi.route("/api/rand-image")
def randImgFunc():
    imgFolfderName = "imgs"
    files = os.listdir(imgFolfderName)
    randFile = random.choice(files)
    return send_file(f"imgs/{randFile}")



randomImgApi.run(host='0.0.0.0')