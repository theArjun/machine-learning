import cv2
import numpy as np
cap=cv2.VideoCapture(0)

face_cascade=cv2.CascadeClassifier(r'/home/arjun/Desktop/workspace/machine-learning/haarcascade_frontalface_alt.xml')
skip=0
face_data=[]
face_section=[]
dataset_path='./sample_data/'
fileName=input("enter the name of the Person")
while True:
	ret,frame=cap.read()
	if ret==False:
 		continue
	gray_frame=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
	faces=face_cascade.detectMultiScale(frame,1.3,5)
	faces=sorted(faces,key=lambda f:f[2]*f[3])
	for (x,y,w,h) in faces[-1:]:
		cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,255),2)
		# crop out the required face : Region Of Interest
		offset=10
		face_section=frame[y-offset:y+h+offset,x-offset:x+w+offset]
		face_section=cv2.resize(face_section,(100,100))
		face_section=np.array(face_section)
		#mat_array = cv.fromarray(face_section)
		skip+=1
		if skip%10==0:
			face_data.append(face_section)
			print(len(face_data))
	cv2.imshow("Frame",frame)
	cv2.imshow("Face_section",face_section)
	key_pressed=cv2.waitKey(1) & 0xFF
	if key_pressed==ord('q'):
 		break
# convert our face_list into numpy array
face_data=np.asarray(face_data)
face_data=face_data.reshape((face_data.shape[0],-1))
print(face_data.shape)
# save into file system
np.save(dataset_path+fileName+'.npy',face_data)
print('Data Successfully saved at',dataset_path+fileName+'.npy')

cap.release()
cv2.destroyAllWindows()