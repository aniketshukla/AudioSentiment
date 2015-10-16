import os
import sys
import MySQLdb
import librosa
import redis
con=MySQLdb.connect("localhost","root","ssww33",'SFAF')
cursor=con.cursor()
r_server=redis.Redis('localhost')







def main():
	add_emotion=raw_input("enter emotion-->")
	add_path=raw_input("enter path-->")
	file_names=os.listdir(add_path)
	for file_name in file_names:
		y,sr= librosa.load(add_path+'/'+file_name)
		print("y sr computed")
		mfcc=librosa.feature.mfcc(y=y,sr=sr)
		print("mfcc computed")
		r_server.rpush(add_emotion,add_emotion+'_'+file_name)
		r_server.rpush(add_emotion+'_'+file_name,[bar for foo in mfcc for bar in foo ])
		print('added')


main()

