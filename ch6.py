# -*- coding: utf-8 -*-

import cv2
import numpy as np

#img=cv2.imread('lena.jpg')
#img1=cv2.rotate(img,0)  #旋转0 90度  1 180度。。。。
#cv2.imshow('img1',img1)
#


#%%
#阈值处理
img=cv2.imread('lena.jpg',0)
t,img1=cv2.threshold(img,127,255,cv2.THRESH_BINARY)


img2=cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,5,0)



t2,img3=cv2.threshold(img,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)  #自动寻找最优阈值，初始阈值设为0
cv2.imshow('img1',img1)
cv2.imshow('img2',img2)
cv2.imshow('img3',img3)

cv2.waitKey()
cv2.destroyAllWindows()



