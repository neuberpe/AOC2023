#fastest boaty alive
with open("AOC6.txt") as file:
	mylist = file.read().splitlines()	#open file with splitlines, shorter then before

time = [int(i) for i in mylist[0].split() if i.isdigit()]
distance = [int(i) for i in mylist[1].split() if i.isdigit()]

res = 1
reach = 0

for i in range(len(time)):				#check if distance in time for each presstime
	for j in range(time[i]):
		if (time[i]-j)*j > distance[i]:
			reach +=1
	res = res*reach						#multiplay sum of possible solutions
	reach=0
print("Teil 1: "+str(res))

t = [str(i) for i in time]				#transform list of numbers into single number
newtime= int("".join(t))
s = [str(i) for i in distance]
newdistance=int("".join(s))

for j in range(newtime):				#same as above
	if (newtime-j)*j > newdistance:
		reach +=1
print("Teil 2: "+str(reach))	
