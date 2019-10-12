# -*- coding: utf-8 -*-

import cv2
import numpy as np


img=cv2.imread('lena.jpg',0)
noise=np.random.randint(0,258,(200,200))*255
noise=noise.astype('uint8')
img2=cv2.add(img,noise)
img3=cv2.blur(img,(5,5))

cv2.imshow('img1',img)
cv2.imshow('img2',img2)
cv2.imshow('img3',img3)

cv2.waitKey()
cv2.destroyAllWindows()
