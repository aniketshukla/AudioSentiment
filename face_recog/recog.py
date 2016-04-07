import cv2
import sys
import os
import time
import sounddevice as sd
MAX_FRAME_RATE=300
DURATION=35
#using nonblocking recorder
#initialising 


def capture():
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
				cv2.rectangle(image_read, (x,y),(x+w,y+w),(255,0,0),2)
			cv2.imshow('12104684',image_read)
			cv2.waitKey(40)
		elif len(faces)==0:
			cv2.imshow('12104684',image_read)
			cv2.waitKey(40)
			print('0 face detected')
		else:
			print('more than one face detected')
			for(x,y,w,h) in faces:
				cv2.rectangle(image_read,(x,y),(x+w,y+w),(255,0,0),2)
			multiple_face_counter=multiple_face_counter+1
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
				cv2.rectangle(image_read, (x,y),(x+w,y+w),(255,0,0),2)
				cv2.imshow('12104684',image_read)
				cv2.waitKey(40)
		
		rval,frame=vc.read()
		fps=fps+1
		print('fps',fps)
	#cv2.waitKey(0)
	

if __name__=='__main__':
	internal()
	


