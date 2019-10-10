#import cv2 as cv
#
##%%
##read image 
#lena=cv.imread('lena.jpg')
#cv.imshow('lena',lena)
#cv.waitKey()
#cv.destroyAllWindows()
#
##%%
#lena=cv.imread('lena.jpg')
#sky=cv.imread('sky.jpg')
#cv.imshow('lena',lena)
#key=cv.waitKey()
#if key==ord('A'):
#    cv.imshow('lena',lena)
#elif key==ord('B'):
#    cv.destroyAllWindows()
#    cv.imshow('sky',sky)
#    key=cv.waitKey()
#
#cv.destroyAllWindows()
#
##save image
#cv.imwrite('sky.png',sky)

#%%
import cv2 
import numpy as np
img=np.zeros((300,300,3),dtype='uint8')
img[:,0:100,0]=255
img[:,100:200,1]=255
img[:,200:300,2]=255
cv2.imshow('img',img)
cv2.waitKey()
cv2.destroyAllWindows()

