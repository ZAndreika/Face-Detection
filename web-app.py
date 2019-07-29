from flask import Flask, render_template, request, redirect, url_for
from flask_caching import Cache
from threading import Thread

from detectors.faceDetector import FaceDetector

import os
import cv2

app = Flask(__name__)
IMG_FOLDER = os.path.join('static', 'img')
app.config['UPLOAD_FOLDER'] = IMG_FOLDER

cache = Cache(app, config = {'CACHE_TYPE': 'simple'})

faceDetector = FaceDetector()

i=0

@app.route('/', methods = ['POST','GET'])
def main():	
	return render_template("index.html")
    
@app.route('/getResult', methods = ['GET'])
def getResult():
	if request.args['type']:
		rtype = request.args['type']
		if rtype == "json":
			json = faceDetector.getDetectedFaceJson()
			return render_template("index.html", json=json)

		elif rtype == "image":
			image = faceDetector.getDetectedFaceImage()

			full_filename = saveImage(image)

			return render_template("index.html", image_src=str(full_filename))

		elif rtype == "exit":
			setLastImageIndex()

		faceDetector.state = request.args['type']		

	return render_template("index.html")

def saveImage(image):
	global i
	full_filename = os.path.join(app.config['UPLOAD_FOLDER'], 'Image' + str(i) + '.jpeg')
	if i > 0: # delete last image in folder
		delete_file_name = os.path.join(app.config['UPLOAD_FOLDER'], 'Image' + str(i-1) + '.jpeg')
		if os.path.isfile(delete_file_name) != 0:
			os.remove(delete_file_name)
	i += 1
	cv2.imwrite(str(full_filename), image) # create new image in folder for transfer to the front
	
	return full_filename

def getLastImageIndex():
	if os.path.isfile("static/current_image_number.txt") != 0:
		f = open("static/current_image_number.txt", "r")
		index = f.read()
		f.close()
	else:
		index = 0

	return int(index)

def setLastImageIndex():
	f = open("static/current_image_number.txt", "w+")
	global i
	f.write(str(i))
	f.close()

if __name__ == "__main__":
	i = getLastImageIndex()

	detector_thread = Thread(target=faceDetector.run)
	detector_thread.start()

	app.run()

	detector_thread.join()