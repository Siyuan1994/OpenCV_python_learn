# -*- coding: utf-8 -*-


import cv2



lena=cv2.imread('lena.jpg')
r1=cv2.pyrDown(lena)
r2=cv2.pyrDown(r1)
r3=cv2.pyrDown(r2)
r4=cv2.pyrDown(r3)

cv2.imshow('1',lena)
cv2.imshow('2',r1)
cv2.imshow('3',r2)
cv2.imshow('4',r3)
cv2.imshow('5',r4)
cv2.waitKey()
cv2.destroyAllWindows()



x1=cv2.pyrUp(lena)
x2=cv2.pyrUp(x1)
x3=cv2.pyrUp(x2)
cv2.imshow('1',lena)
cv2.imshow('2',x1)
cv2.imshow('3',x2)
cv2.imshow('4',x3)

cv2.waitKey()
cv2.destroyAllWindows()
