#testing co-relativity of data with clustering
from numpy import array
from scipy.cluster.vq import vq,kmeans,whiten
import redis
import numpy
from random import choice
con=redis.Redis('localhost')
parameters=['happy','angry','unhapppy','neutral']
error_cluster=[0]*len(parameters)
#have to hack into 
value_parameters=[[],[],[],[]]
value_parameters_error=[]
value_parameters_length=[0,0,0,0]
universal=[]
#def inverse_hashing():
count=0
for i,j in zip(range(0,len(parameters)),parameters):
	foo=con.lrange(j,0,-1)
	for bar in foo:
		temp=map(np.float64,con.lrange(bar,0,-1))
		if (len(temp)!=1292):
			continue
		value_parameters[i].append(count)
		value_parameters_length[i]=value_parameters_length[i]+1
		count=count+1
		universal.append(temp)


universal=np.array(universal)
#wont be using wighten to reduce computation
kmeans_result=kmeans(universal,len(parameters))

code,distortion=vq(universal,kmeans_result[0])

total_cases=len(universal)
wrongly_matched=0
pointer=0
#introducing cluster mismatch a fast cluster error detection algorithm
counter=0
counter1=0
while counter<len(parameters):
	code_inside=code[counter1:counter1+value_parameters_length[counter]]
	error_inside=[0]*len(parameters)
	for foo in code_inside:
		error_inside[foo]=error_inside[foo]+1
	value_parameters_error.append(error_inside)
	counter=counter+1
	counter1=counter1+value_parameters_length[counter-1]


for j in value_parameters_error:
	j.sort()
count1=0
for j in value_parameters_error:
	if sum(j)==0:
		continue
	print(sum(j[0:-2]))
	print(sum(j))
	error_cluster[count1]=float(sum(j[0:-2]))/float(sum(j))
	count1=count1+1


error_final1=sum(error_cluster)/len(parameters)
error_final2=max(error_cluster)




