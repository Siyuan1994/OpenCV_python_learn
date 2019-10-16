# -*- coding: utf-8 -*-

import cv2
import numpy as np

num1=cv2.imread('4.png')
cv2.imshow('origin',num1)
num1=cv2.cvtColor(num1,cv2.COLOR_RGB2GRAY)
a,b=cv2.threshold(num1,127,255,cv2.THRESH_BINARY)
contou,hier=cv2.findContours(b,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
ss=np.zeros_like(num1)
o=cv2.drawContours(ss,contou,-1,(255,25521,255),5)
cv2.imshow('result',ss)
cv2.waitKey()
cv2.destroyAllWindows()

n=len(contou)
cont=[]
for i in range(n):
    temp=np.zeros(num1.shape,np.uint8)
    cont.append(temp)
    cont[i]=cv2.drawContours(cont[i],contou,i,(255,255,255),5)
    cv2.imshow(str(i),cont[i])
    
cv2.waitKey()    
cv2.destroyAllWindows()



num1=cv2.imread('4.png')
#cv2.imshow('origin',num1)
num1=cv2.cvtColor(num1,cv2.COLOR_RGB2GRAY)
a,b=cv2.threshold(num1,127,255,cv2.THRESH_BINARY)
contou,hier=cv2.findContours(b,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)
(x,y),r=cv2.minEnclosingCircle(contou[0])
center=(int(x),int(y))
r=int(r)
b=cv2.cvtColor(num1,cv2.COLOR_BAYER_GR2RGB)
cv2.circle(b,center,r,(0,255,255),2)
cv2.imshow('re',b)
cv2.waitKey()
cv2.destroyAllWindows()

