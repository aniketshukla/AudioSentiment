from pybrain.datasets            import ClassificationDataSet
from pybrain.utilities           import percentError
from pybrain.tools.shortcuts     import buildNetwork
from pybrain.supervised.trainers import BackpropTrainer
from pybrain.structure.modules   import SoftmaxLayer
from pylab import ion, ioff, figure, draw, contourf, clf, show, hold, plot
from scipy import diag, arange, meshgrid, where
from numpy.random import multivariate_normal
from pybrain.tools.xml.networkwriter import NetworkWriter
from pybrain.tools.xml.networkreader import NetworkReader
import redis
import os
r_server=redis.Redis('localhost')
ds=ClassificationDataSet(1292,nb_classes=2,class_labels=['happy','angry'])

def dataset__generator(emotion):
	emotion['happy']=0
	emotion['angry']=1
	#emotion['neutral']=[3]
	#emotion['unhappy']=[4]
	for foo in emotion:
		for bar in r_server.lrange(foo,0,-1):	
			if r_server.llen(bar)!=1292:
				print("skipping "+bar)
				continue		
			ds.addSample(map(float,r_server.lrange(bar,0,-1)),emotion[foo])


def main():
	emotion={}
	dataset__generator(emotion)
	print('dataset generated')
	tstdata,trndata=ds.splitWithProportion(0.25)
	print('data splitted')
	#ds.getLength()
	trndata._convertToOneOfMany( )
	tstdata._convertToOneOfMany( )
	emotion={}
	if os.path.isfile('train.xml'):
		fnn=NetworkReader.readFrom('train.xml')
	else:
		fnn=buildNetwork(1292,1,2,outclass=SoftmaxLayer)
	NetworkWriter.writeToFile(fnn, 'train.xml')
	print('starting training')
	trainer=BackpropTrainer(fnn,dataset=trndata,momentum=0.1,verbose=True,weightdecay=0.01)	
	
	print('epoch level '+str(1000))
	trainer.trainEpochs(216000)
	NetworkWriter.writeToFile(fnn, 'train.xml')
	#trnresult=percentError(trainer.testOnData(),trndata['class'])
	#tstresult=percentError(trainer.testOnClassData(dataset=tstdata),tstdata['class'])
	r_server.set('errortest'+str(i),tstresult)
	r_server.set('errortrain'+str(i),trnresult)



main()