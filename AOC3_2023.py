#find all numbners adjacent to symbols and sum them and then find all duo numbers around a * and add their multiple

with open("AOC3.txt") as file:
	mylist = file.read().splitlines()
numbers ="0123456789"
symbols ="*#+$%@&-/="

sym=[]
value=[]
num=[]
dummy = ""
x = 0
y= 0

for i in mylist:	#create a position list with number and a position list with symbols
	for j in i:
		if j in numbers:
			dummy += str(j)
			value.append([x,y])
		elif j in symbols:
			sym.append([x,y])
			if len(dummy) != 0:
				value.append(int(dummy))
				dummy= ""
				num.append(value)
				value=[]
		else:
			if len(dummy) != 0:
				value.append(int(dummy))
				dummy= ""
				num.append(value)
				value=[]
		x+=1
	x = 0
	y += 1
if len(dummy) != 0:		#bugfixing because last number, still dont know WHY there are not more errors
	value.append(int(dummy))
	dummy= ""
	num.append(value)
	value=[]	

adjacent=[]		#expand the position list of symbols to ADJECENT position
for k in sym:
	for m in range(-1,2,1):
		for o in range(-1,2,1):
			adjacent.append([k[0]+m,k[1]+o])

a = False
res = []
for k in num:		#if 1 pos. of a number is adjecent to symbol add up
	for f in range(len(k)-1):
		if k[f] in adjacent:
			a = True
	if a ==True:
		res.append(k[-1])
		a = False

print(sum(res))

star=[]
x = 0
y= 0
for i in mylist:	#find all * positions into a list
	for j in i:
		if j == "*":
			star.append([x,y])		
		x+=1
	x = 0
	y += 1

starjacent=[]
value=[]
for k in star:		#make a adjecent list
	for m in range(-1,2,1):
		for o in range(-1,2,1):
			value.append([k[0]+m,k[1]+o])
	starjacent.append(value)
	value=[]

a = False
res = []
starres=[]		#find all numbers around a star, if there are exactly 2, multiply and save em
for n in starjacent:
	for k in num:
		for f in range(len(k)-1):
			if k[f] in n:
				a = True
		if a ==True:
			res.append(k[-1])
			a = False
	if len(res) == 2:
		starres.append(res[0]*res[1])
	res=[]

print(sum(starres))