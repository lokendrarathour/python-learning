import cv2
import numpy as np
import matplotlib.pyplot as plt
import numpy as np
%matplotlib inline

def draw_circle(event,x,y,flags,param):
    if event == cv2.EVENT_RBUTTONDBLCLK:
        cv2.circle(img_1,(x,y),100,color=(0,0,255),thickness=10)
        
cv2.namedWindow(winname="dog")
cv2.setMouseCallback("dog",draw_circle)

img_1 = cv2.imread('one.jpeg')

while True:
    cv2.imshow('dog',img_1)
    
    if cv2.waitKey(20) & 0xFF == 27:
        break
        
cv2.destroyAllWindows()

