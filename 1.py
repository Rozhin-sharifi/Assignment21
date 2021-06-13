import numpy as np
import cv2

x=160
y=160

image=np.zeros((x,y))

for i in range (0,x,20):
        if i%2==0:
            for j in range (0,y,20):
                if j%2==0:
                    image[i:i+20,j:j+20]=np.zeros((20,20))
                else:
                    image[i:i+20,j:j+20]=np.ones((20,20))*255
        else:
            for j in range (0,y,20):
                if j%2==0:
                    image[i:i+20,j:j+20]=np.zeros((20,20))
                else:
                    image[i:i+20,j:j+20]=np.ones((20,20))*255
cv2.imshow('Picture',image)
cv2.waitKey()
