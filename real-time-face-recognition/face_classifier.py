import numpy as np
import cv2
import os

# Algorithm

def distance(x1,x2):
	return np.sqrt(np.sum((x1-x2)**2))
def KNN(X,Y,query_point,k=5):
	m=X.shape[0]
	val=[]
	for i in range(m):
		d=distance(X[i],query_point)
		val.append((d,Y[i]))
	val=sorted(val)
	val=val[:k]
	val=np.array(val)
	new_val=np.unique(val[:,1],return_counts=True)
	index=new_val[1].argmax()
	pred=new_val[0][index]
	return pred

cap=cv2.VideoCapture(0)
face_cascade=cv2.CascadeClassifier(r'/home/arjun/Desktop/workspace/machine-learning/haarcascade_frontalface_alt.xml')
face_data=[]
dataset_path='./sample_data/'
skip=0
label=[] 
class_id=0  # labels for the given file
names={} # mapping between id and name

# Data Preparation
for fx in os.listdir(dataset_path):
	if fx.endswith('.npy'):
		names[class_id]=fx[:-4]
		data_item=np.load(dataset_path+fx)
		face_data.append(data_item)
		# create labels
		target=class_id*np.ones((data_item.shape[0],))
		label.append(target)
		class_id+=1
face_dataset=np.concatenate(face_data,axis=0)
face_labels=np.concatenate(label,axis=0).reshape((-1,1))
print(face_dataset.shape)
print(face_labels.shape)

# Testing

while True:
	ret,frame=cap.read()
	faces=face_cascade.detectMultiScale(frame,1.3,5)
	for (x,y,w,h) in faces:
		offset=10
		face_section=frame[y-offset:y+h+offset,x-offset:x+w+offset]
		face_section=cv2.resize(face_section,(100,100))
		face_section=np.array(face_section)
		out=KNN(face_dataset,face_labels,face_section.flatten())
		pred_name=names[int(out)]
		cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,255),2)
		cv2.putText(frame,pred_name,(x,y-offset),cv2.FONT_HERSHEY_SIMPLEX,1,(255,0,0),2,cv2.LINE_AA)
	cv2.imshow("Faces",frame)
	key_pressed=cv2.waitKey(1) & 0xFF
	if key_pressed==ord('q'):
		break
cap.release()
cv2.destroyAllWindows()







