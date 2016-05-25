import cv2
import sys
import os
import time
import sounddevice as sd
import numpy as np
from os import listdir
import matplotlib.image as img1
import time
MAX_FRAME_RATE=300
DURATION=35
#using nonblocking recorder
#initialising 



def predicter(recognizer,imager):
	nbr=recognizer.predict(imager)
	print("--------------<>",nbr)
	if nbr[0]==0:
		return 1
	else:
		return 0

def img_random():
	cascade="/home/aniket/Desktop/code/face_recog/haarcascade_classifier/smile.xml"
	img_captured=[]
	faceCascade=cv2.CascadeClassifier(cascade)
	path='/home/aniket/Desktop/code/AudioSentiment/face_recog/yalefaces'
	img_list=os.listdir(path)
	for foo in img_list:
		gray=img1.imread(path+'/'+foo)
		#print(gray)
		faces=faceCascade.detectMultiScale(
		gray,
		scaleFactor=1.2,
		minNeighbors=5,
		minSize=(30,30),
		flags=cv2.cv.CV_HAAR_SCALE_IMAGE,
		)
		for(x,y,w,h) in faces:
			img_captured.append(gray[y:(y+h),x:(x+w)])
	return img_captured
		



	


def face_trainer(counter):
	img_alter=[]
	img_captured=[]
	fps=0
	vc=cv2.VideoCapture(0)
	rval,frame=vc.read()
	cascade="/home/aniket/Desktop/code/face_recog/haarcascade_classifier/smile.xml"

	while rval:
		counter=counter-1
		if counter==0:
			break
		
		faceCascade=cv2.CascadeClassifier(cascade)
		image_read=frame
		gray=cv2.cvtColor(image_read,cv2.COLOR_BGR2GRAY)
		faces=faceCascade.detectMultiScale(
		gray,
		scaleFactor=1.2,
		minNeighbors=5,
		minSize=(30,30),
		flags=cv2.cv.CV_HAAR_SCALE_IMAGE,
		)
		print('found '+str(len(faces))+
		' in this image \n plotting image')
		for(x,y,w,h) in faces:
			cv2.rectangle(image_read, (x,y),(x+w,y+h),(255,0,0),2)
			img_captured.append(gray[y:(y+h),x:(x+w)])
		cv2.imshow('Sit still while we train this software for your face',image_read)
		cv2.waitKey(40)
		
		
		fps=fps+1
		print('fps',fps)
		rval,frame=vc.read()
	labels=[0]*len(img_captured)
	img_alter=img_random()
	for foo in img_alter:
		img_captured.append(foo)
		labels.append(1)
	return img_captured,labels
	#cv2.waitKey(0)



def capture():
	img_array,labels=face_trainer(100)
	print(labels)
	time.sleep(10)
	recognizer=cv2.createLBPHFaceRecognizer()
	recognizer.train(img_array,np.array(labels))
	frame_count=0
	duration=DURATION
	sd.default.samplerate=22050
	sd.default.channels=1
	myrecording=sd.rec(duration*22050)
	vc=cv2.VideoCapture(0)
	cascade="/home/aniket/Desktop/code/face_recog/haarcascade_classifier/smile.xml"
	rval,frame=vc.read()
	
#path2='/'.join(cascade.split('/')[1:-1])
#print(path2)
#print(os.listdir('/home/aniket/Desktop/code/face_recog/'))

	multiple_face_counter=0
	while rval:
		print('current frame count',frame_count)
		print(multiple_face_counter)
		faceCascade=cv2.CascadeClassifier(cascade)
		image_read=frame
#cv2.imshow("smile found",image_read)

#turning image to grayscale
		gray=cv2.cvtColor(image_read,cv2.COLOR_BGR2GRAY)
		faces=faceCascade.detectMultiScale(
		gray,
		scaleFactor=1.2,
		minNeighbors=5,
		minSize=(30,30),
		flags=cv2.cv.CV_HAAR_SCALE_IMAGE,
		)
	
	
		print('found '+str(len(faces))+
		' in this image \n plotting image')

		if len(faces)==1:
			for(x,y,w,h) in faces:
				if predicter(recognizer,gray[y:(y+h),x:(x+w)])==1:
					cv2.rectangle(image_read, (x,y),(x+w,y+h),(255,0,255),2)
				else:	
					cv2.rectangle(image_read, (x,y),(x+w,y+h),(255,0,0),2)
					multiple_face_counter=multiple_face_counter+1
			cv2.imshow('12104684',image_read)
			cv2.waitKey(40)
		elif len(faces)==0:
			cv2.imshow('12104684',image_read)
			cv2.waitKey(40)
			print('0 face detected')
		else:
			print('more than one face detected')
			for(x,y,w,h) in faces:
				if predicter(recognizer,gray[y:(y+h),x:(x+w)])==1:
					cv2.rectangle(image_read, (x,y),(x+w,y+h),(255,0,255),2)
				else:	
					cv2.rectangle(image_read, (x,y),(x+w,y+h),(255,0,0),2)
					multiple_face_counter=multiple_face_counter+1
			#multiple_face_counter=multiple_face_counter+1
			cv2.imshow("12104684",image_read)
			cv2.waitKey(40)
			try:
				if multiple_face_counter>20:
					a=1/0
			except:
				print('more than one face detected')
		rval,frame=vc.read()
		frame_count=frame_count+1
		if frame_count>MAX_FRAME_RATE:
			break
	return myrecording

		
def internal():
	fps=0
	vc=cv2.VideoCapture(0)

	rval,frame=vc.read()
	try:
		alter=sys.argv[1]
	except :
		print(BaseException('no scale factor was provided'))
	cascade="/home/aniket/Desktop/code/face_recog/haarcascade_classifier/smile.xml"

#path2='/'.join(cascade.split('/')[1:-1])
#print(path2)
#print(os.listdir('/home/aniket/Desktop/code/face_recog/'))

	multiple_face_counter=0
	while rval:
		print(multiple_face_counter)
		faceCascade=cv2.CascadeClassifier(cascade)
		image_read=frame
#cv2.imshow("smile found",image_read)

#turning image to grayscale
		gray=cv2.cvtColor(image_read,cv2.COLOR_BGR2GRAY)
		faces=faceCascade.detectMultiScale(
		gray,
		scaleFactor=1.2,
		minNeighbors=5,
		minSize=(30,30),
		flags=cv2.cv.CV_HAAR_SCALE_IMAGE,
		)
	
	
		cv2.imshow("please ensure that there's only one person in the image",image_read)
		cv2.waitKey(40)
		print('found '+str(len(faces))+
		' in this image \n plotting image')
		for(x,y,w,h) in faces:
				cv2.rectangle(image_read, (x,y),(x+w,y+h),(255,0,0),2)
				cv2.imshow('12104684',image_read)
				cv2.waitKey(40)
		
		rval,frame=vc.read()
		fps=fps+1
		print('fps',fps)
	#cv2.waitKey(0)
	

if __name__=='__main__':
	capture()
	


