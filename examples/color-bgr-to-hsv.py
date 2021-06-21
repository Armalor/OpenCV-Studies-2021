import cv2
import numpy as np

colors = {'clr': np.uint8 ([[[5,0,0]]])}


for color, value in colors.items():
    hsv = cv2.cvtColor(value, cv2.COLOR_BGR2HSV)
    print(colors['clr'], hsv, sep=' => ')

