#fastest boaty alive
with open("AOC6.txt") as file:
	mylist = file.read().splitlines()	#open file with splitlines, shorter then before

time = [int(i) for i in mylist[0].split() if i.isdigit()]
distance = [int(i) for i in mylist[1].split() if i.isdigit()]

boat = [] # distances per round
split = []
res = 1
reach = 0

for i in range(len(time)):
	for j in range(time[i]):
		split.append((time[i]-j)*j)
	boat.append(split)
	split=[]

for i,k in enumerate(boat):		#find # of possibilites to achieve min distance
	for a in k:
		if a > distance[i]:
			reach +=1
	res = res*reach
	reach=0

print("Teil 1: "+str(res))

newtime=""
for e in time:
	newtime += str(e)
newtime= int(newtime)

newdistance=""
for e in distance:
	newdistance += str(e)
newdistance = int(newdistance)	#only one time and one distance

for j in range(newtime):		#bruteforce
	split.append((newtime-j)*j)
for k in split:
	if k > newdistance:
		reach +=1
print("Teil 2: "+str(reach))	
