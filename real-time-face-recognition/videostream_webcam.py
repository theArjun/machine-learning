'''
    Title - Open CV Basics - Working with Video Stream from Webcam
    Author -  Arjun Adhikari
    Date - June 16, 2019
'''

import cv2

# 0 is the default video capturing device set to computer.
cap = cv2.VideoCapture(0)

while True:

    ret, frame = cap.read()

    # For gray Frame
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    if ret == False:
        continue

    cv2.imshow('Video Frame', frame)
    # cv2.imshow('Video Frame', gray_frame)


    # Wait for user input 'q', then stop the loop.
    # Masking with 0xFF will convert 32 bit number into 8 bit number.
    key_pressed = cv2.waitKey(1) & 0xFF
    if key_pressed == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
