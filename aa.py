import numpy as np
import cv2
img = cv2.imread("C:\\Users\\Akash\\Pictures\\hulk.JPG")
kernel = np.ones((5,5),np.uint8)


imggray = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
imgblur =  cv2.GaussianBlur(img,(5,5),0)
imgcanny = cv2.Canny(img,100,100)
imgdia = cv2.dilate(imgcanny,kernel,iterations=1)
imgero = cv2.erode(imgdia,kernel,iterations=1)
imgcrp = img[200:700,200:500]

cv2.imshow("",imggray)
cv2.waitKey(500)
cv2.imshow("",imgblur)
cv2.waitKey(500)
cv2.imshow("",imgcanny)
cv2.waitKey(500)
cv2.imshow("",imgdia)
cv2.waitKey(500)
cv2.imshow("",imgero)
cv2.waitKey(500)

print(img.shape)
imgresize = cv2.resize(img,(600,1200))
cv2.imshow("",imgresize)
cv2.waitKey(500)
cv2.imshow("",imgcrp)
cv2.waitKey(1000)
cv2.imshow("",img)
cv2.waitKey(500)