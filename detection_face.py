import numpy as np
import cv2
cascadeClassifierPath =r'C:\Users\miken\Documents\Codex_Python\cv2\data\haarcascade_frontalface_alt.xml'

cascadeClassifier = cv2.CascadeClassifier(cascadeClassifierPath)
path = r'C:\Users\miken\Documents\Codex_Python\source.jpg'
img =cv2.imread(path)
grayImage = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
detectedFaces = cascadeClassifier.detectMultiScale(grayImage)
for(x,y,width,height) in detectedFaces:
    cv2.rectangle(img,(x,y),(x+width,y+height),(0,255,0),5)
    cv2.imwrite(r'C:\Users\miken\Documents\Codex_Python\source_face.jpg',img)
