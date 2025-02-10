import cv2
import matplotlib.pyplot as plt
import time
import os
import imutils
import numpy as np
from model import model
import requests
from cvt import get_image_handler as img_cvt
import json

font = cv2.FONT_HERSHEY_SIMPLEX
fontScale = 1
color = (255, 0, 0)
thickness = 2

cam =  cv2.VideoCapture(0)
while True :
    time.sleep(0.03)


    for i in range(10) :
        ret , frame = cam.read()
    frame = frame
    output = model(frame)      
    print(output)
    if output :
        _object = output[0]
        xLeftTop = output[1]
        yLeftTop = output[2]
        xRightBottom = output[3]
        yRightBottom = output[4]
        cv2.rectangle(frame, (xLeftTop, yLeftTop), (xRightBottom, yRightBottom), (0, 255, 0), 2)
    
        cv2.putText(frame, _object, (xLeftTop , yLeftTop-15), font,fontScale, color, thickness, cv2.LINE_AA)
    
    else :
        print("--NO LICENSE DETECTED--")
    
    cv2.imshow("cam",frame)
    if cv2.waitKey(1) == ord('q'):
        break
cam.release()
cv2.destroyAllWindows()

