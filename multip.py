import multiprocessing as mp
import time
import sys
import os
from face_recog.recog import capture
import sounddevice as sd
from pybrain.tools.xml.networkwriter import NetworkWriter
from pybrain.tools.xml.networkreader import NetworkReader
import librosa
import numpy as np
FNN_PATH='train.xml'


def mapper(mfcc):
	return mfcc[-1292:]



def main():
	audio=capture()
	audio=np.transpose(audio)[0]
	#sd.play(audio,44100,blocking=True)
	mfcc=librosa.feature.mfcc(y=audio,sr=22050,n_mfcc=13)
	#print(np.shape(mfcc))
	mfcc=np.array(map(mapper,mfcc))
	#print(mfcc)
	mfcc=mfcc.max(axis=0)
	#print(np.shape(mfcc))
	#print(mfcc)
	fnn=NetworkReader.readFrom(FNN_PATH)
	#print(fnn)
	fnn=fnn.activate(mfcc)
	max_index=0
	max_value=fnn[0]
	for foo in range(1,len(fnn)):
		if fnn[foo]>max_value:
			max_index=foo
			max_value=fnn[foo]
	if max_index==0:
		print '{"emotion":"Happy"}'
	elif max_index==1:
		print '{"emotion":"Angry"}'

	


if __name__=='__main__':
	main()

