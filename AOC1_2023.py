#Erste und Letzte Zahl finden, daraus 2.stellige Zahl bilden, Summe dieser ist Ergebnis

with open("AOC1.txt", "r") as file:
    data = file.read().replace("\n", ",")
mylist = data.split(",") #transormieren des obigen strings in liste, gesplittet nach ","
num ="0123456789" #was sind zahlen
words=["one","two","three","four","five","six","seven","eight","nine"]

res =[] #ergebins
for k in mylist:
	value =[] #zwischenergebnis
	for i in k:	
		if i in num: #nummern check
			value.append(int(i))
	res.append(value[0]*10+value[-1]) #mal 10 der ersten stelle plus einer stelle

print("Ergebnis Teil 1: "+str(sum(res)))

res=[]
for k in mylist:
	pos=0
	value =[]
	for i in k:
		if i in num:
			value.append(int(i))
		elif len(k[pos:]) >= 3:
			for m in words:
				if m in k[pos:pos+len(m)]:
					value.append(words.index(m)+1)
		else:
			pass
		pos +=1
	res.append(value[0]*10+value[-1])

print("Ergebnis Teil 2: "+str(sum(res)))
