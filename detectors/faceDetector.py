import cv2
from threading import Thread
import json

class FaceDetector:

    def __init__(self):
        self.faceCascade = cv2.CascadeClassifier('haarcascades\\haarcascade_frontalface_default.xml')
        self.video_capture = cv2.VideoCapture(0)
        self.state = ""
        

    def run(self):
        while True:
            _, self.img = self.video_capture.read()

            if self.state == "exit":
                break

        self.video_capture.release()
        cv2.destroyAllWindows()

    def getFaceImage(self, img):
        gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) # convert image to grey
        gray_img = cv2.equalizeHist(gray_img) # normalize gray image
        faces = self.faceCascade.detectMultiScale(gray_img, scaleFactor= 1.1, minNeighbors= 2, minSize=(30, 30)) # detect faces

        for (x, y, width, height) in faces:
            cv2.rectangle(img, (x,y), (x+width, y+height), (0,255,0), 2)

        return img

    def getFaceJson(self, img):
        gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) # convert image to grey
        gray_img = cv2.equalizeHist(gray_img) # normalize gray image
        features = self.faceCascade.detectMultiScale(gray_img, scaleFactor= 1.1, minNeighbors= 2, minSize=(30, 30)) # detect faces
        
        coords = []
        for (x, y, width, height) in features: # add data about faces to list
            coords.append({"x":int(x), "y":int(y), "width":int(width), "height":int(height)})

        return json.dumps(coords) # convert list to json

    def getDetectedFaceJson(self):
        return self.getFaceJson(self.img)

    def getDetectedFaceImage(self):
        return self.getFaceImage(self.img)

if __name__ == "__main__":
    faceCascade = cv2.CascadeClassifier('..\\haarcascades\\haarcascade_frontalface_default.xml')
    video_capture = cv2.VideoCapture(0)

    while True:
            _, img = video_capture.read()

            gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            gray_img = cv2.equalizeHist(gray_img)
            faces = faceCascade.detectMultiScale(gray_img, scaleFactor= 1.1, minNeighbors= 2, minSize=(30, 30))

            for (x, y, width, height) in faces:
                cv2.rectangle(img, (x,y), (x+width, y+height), (0,255,0), 2)

            cv2.imshow("Press Enter for exit", img)

            if(cv2.waitKey(1) == 13):
                break

