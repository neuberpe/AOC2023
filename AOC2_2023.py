#maximale anzahl an wuerfel pro spiel finden und gegen grenze testen oder min menge multiplizieren

with open("AOC2.txt", "r") as file:
    data = file.read().replace("\n", "|")
mylist = data.split("|") #transormieren des obigen strings in liste, gesplittet nach ","

color =["red", "green","blue"]
limit =[12,13,14]
idnr = 1
value=[]
power=[]

for k in mylist:
	res = []
	for n in range(3):
		highest = []
		pos = [i for i in range(len(k)) if k.startswith(color[n],i)]
		for m in pos:
			highest.append(k[m-3:m-1])
		try:
			res.append(max(highest))
		except:
			res.append(0)
	res = [int(e) for e in res]
	if res[0] <= limit[0] and res[1] <= limit[1] and res[2] <= limit[2]:
		value.append(idnr)
	power.append(res[0]*res[1]*res[2])
	idnr +=1

print("Teil 1: " +str(sum(value)))
print("Teil 2: " +str(sum(power)))