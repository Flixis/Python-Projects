# !/usr/bin/python
#requires opencv2 and numpy
import cv2
import numpy as np

#Load Image to test in
img_rgb = cv2.imread('C:\Programming\python\Python-Projects\OpenCV\Testimage.JPG')
img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
#debug
print("Test Image to gray:")
print(img_rgb)
########

#load template image in
template = cv2.imread('C:\Programming\python\Python-Projects\OpenCV\Template.JPG',0)
#debug
print("Template image:")
print(template)
########

#get widht and height of template itterate through it
w, h = template.shape[::-1]
#Set resolution
res = cv2.matchTemplate(img_gray,template,cv2.TM_CCOEFF_NORMED)
#Setting threshold for matching
threshold = 0.5
loc = np.where( res >= threshold)



#Create yellow box around matching image
for pt in zip(*loc[::-1]):
    cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0,255,255), 2)


#Display window with following paramaters
cv2.namedWindow('detected',cv2.WINDOW_NORMAL)
cv2.imshow('detected',img_rgb)
cv2.resizeWindow('detected', 1280,720)
cv2.waitKey()