""" 
11:27:01 19 Jul, 2019 by Arjun Adhikari
Loading images with OpenCV
"""
import cv2
img=cv2.imread(r'/home/arjun/Desktop/workspace/machine-learning/logo.png')
new_img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
gray=cv2.imread(r'/home/arjun/Desktop/workspace/machine-learning/logo.png',cv2.IMREAD_GRAYSCALE)
cv2.imshow("Flower",img)
cv2.imshow("Gray",gray)
cv2.waitKey(0)
cv2.destroyAllWindows()