'''
    Title - Open CV Basics - Displaying Image in opencv2
    Author -  Arjun Adhikari
    Date - June 15, 2019
'''

import cv2

# Read Image
img = cv2.imread('man.jpg')

# Display Image
cv2.imshow('Man Image', img)

''' Waiting Time
    - 0 refers to wait infinitely.
    - 25 refers to wait for 25 miliseconds and quit.
    - 350 refers to wait for 0.35 seconds and quit.
'''
cv2.waitKey(3000)


# Read Image in Different Color Mode

img  = cv2.imread('man.jpg', cv2.IMREAD_GRAYSCALE)

cv2.imshow('Grayscale Man Image', img)
cv2.waitKey(10000)


#Destroy Windows
cv2.destroyAllWindows()