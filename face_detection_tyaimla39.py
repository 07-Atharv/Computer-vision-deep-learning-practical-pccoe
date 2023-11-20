# -*- coding: utf-8 -*-
"""Face_detection_TYAIMLA39

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Qvjre6wyqCBnvFWblRVIm8aFrsL-TNpM

## **Face Detection**
"""

from PIL import Image

def get_image_data():
    faces = []
    ids = []
    image = Image.open(path).convert('L')
    image_np = np.array(image, 'uint8')
    id = 1
    ids.append(id)
    faces.append(image_np)
    return np.array(ids), faces

ids, faces = get_image_data()

import os
import cv2
import zipfile
import numpy as np
from google.colab.patches import cv2_imshow

from google.colab import drive
drive.mount('/content/drive')

path = "/content/drive/MyDrive/yalefaces/train/subject03.surprised.gif"

lbph_classifier = cv2.face.LBPHFaceRecognizer_create()
lbph_classifier.train(faces,ids)
lbph_classifier.write('lbph_classifier.yml')

lbph_face_classifier = cv2.face.LBPHFaceRecognizer_create()
lbph_face_classifier.read("/content/lbph_classifier.yml")
test_image = path
image = Image.open(test_image).convert('L')
image_np = np.array(image,'uint8')
#cv2_imshow(image_np)
predictions = lbph_face_classifier.predict(image_np)
print(predictions)
expected_output = 1
print(expected_output)
cv2.putText(image_np, 'Pred.' +str(predictions[0]),(10,30),
            cv2.FONT_HERSHEY_COMPLEX_SMALL,1,(0,255,0))
cv2.putText(image_np, 'Expec.' +str(expected_output),(10,50),
            cv2.FONT_HERSHEY_COMPLEX_SMALL,1,(0,255,0))
cv2_imshow(image_np)