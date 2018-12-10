# -*- coding: utf-8 -*-
"""
Created on Mon Dec 10 17:19:16 2018

@author: Sarath.Sahadevan
"""

import cv2
import numpy as np

device = cv2.VideoCapture(0)
while True:
    ret,frame = device.read()
    hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    lower_range = np.array([10,100,20])
    upper_range = np.array([25,255,255])
    
    mask  = cv2.inRange(hsv,lower_range,upper_range)
    
    #cv2.imshow("frames",frame)
    
    result = cv2.bitwise_and(frame,frame,mask = mask)

    cv2.imshow("masked",result)

    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
device.release()
cv2.destroyAllWindows()