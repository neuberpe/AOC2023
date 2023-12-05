#grind through transformation tables and get lowest, part 2 f... 
import re

with open("AOC5.txt") as file:
	mylist = file.read().splitlines()	#open file with splitlines, shorter then before

#sample=[[2,3],[3,7],[4,12],[2,18],[3,22],[2,27],[2,31]]		#sample
sample =[[16,3],[33,21],[26,56],[38,84],[10,124],[37,136],[22,175]]		#input

#get all the lists, position manually because idgaf
seed=[]
seedlocation=[]
seed.append(re.findall(r"\d+",mylist[0]))
seed = [int(e) for e in seed[0]]
seedlocation.append(seed)
franz = False

transform=[]		#build the transformation table
x=[]
for c in range(7):
	for a in range(sample[c][0]):
		x.append(re.findall(r"\d+",mylist[a+sample[c][1]]))
	transform.append(x)
	x=[]

for i in range(len(transform)):		#grind through
	for a in seedlocation[i]:
		franz= False
		for b in transform[i]:
			c= int(a)-int(b[1])
			d= int(b[2])-c
			if c >= 0 and d> 0:
				x.append(int(a)+int(b[0])-int(b[1]))
				franz= True
		if franz == False:
			x.append(a)
	seedlocation.append(x)
	x=[]

print("Teil 1: "+str(min(seedlocation[7])))