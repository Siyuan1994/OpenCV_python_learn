# -*- coding: utf-8 -*-
import cv2
import numpy as np


lena=cv2.imread('lena.jpg')

#缩放
#%%

lena1=cv2.resize(lena,(300,100))
cv2.imshow('lena1',lena1)
cv2.imshow('lena',lena)
cv2.waitKey()
cv2.destroyAllWindows()