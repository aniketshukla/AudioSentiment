from flask import Flask,render_template,request,session,g,redirect,url_for,send_from_directory
from flask import abort,render_template,flash,make_response 
from flask_restful import Resource,Api
import os
import json
from pybrain.tools.xml.networkwriter import NetworkWriter
from pybrain.tools.xml.networkreader import NetworkReader
import pybrain
import warnings
import librosa
import numpy as np
with warnings.catch_warnings():
    warnings.warn("ignore")
import random
from pydub import AudioSegment
from werkzeug import secure_filename
UPLOAD_PATH=os.getcwd()+"/static/music_repository"



DEBUG=True
SECRET_KEY='root'
USERNAME='aniket'
PASSWORD='root'
FNN_PATH='../train.xml'
app=Flask(__name__)
api=Api(app)
app.config['UPLOAD_FOLDER']=UPLOAD_PATH
app.debug=True
FNN_PATH='../train.xml'

def mapper(mfcc):
	return mfcc[-1292:]


@app.route('/')
def adder():
	return render_template('panel.html')




@app.route('/sent',methods=['POST'])
def getSent():
	return 1
	if request.method!='POST':
		return '{emotion:invalid request method submit a post request}'
	voice=request.files['file']
	filename=secure_filename(voice.filename)	
	format_audio=request.form['audio_format']
	path=os.path.join(app.config['UPLOAD_FOLDER'],filename)
	voice.save(path)
	temp="AudioSegment.from_"+str(format_audio)+"('"+path+"')"
	temp=eval(temp)
	os.remove(path)
	temp.export(path,format="mp3",bitrate="64k")
	try:
		y,sr=librosa.load(path)
	except:
		return "{emotion:error}"
	os.remove(path)	
	print('y sr computed')
	mfcc=librosa.feature.mfcc(y=y,sr=sr,n_mfcc=13)
	mfcc=np.array(map(mapper,mfcc))
	mfcc=mfcc.max(axis=0)
	fnn=NetworkReader.readFrom(FNN_PATH)
	fnn=fnn.activate(mfcc)
	max_index=0
	max_value=fnn[0]
	for foo in range(1,len(fnn)):
		if fnn[foo]>max:
			max_index=foo
			max_value=fnn[foo]
	if max_index==0:
		return "{emotion:Happy}"
	elif max_index==1:
		return "{emotion:Angry}"



@app.route('/getXML')
def givemeXML():
	return send_from_directory('../','train.xml',as_attachment=True)



		


if __name__=='__main__':
	app.run()


