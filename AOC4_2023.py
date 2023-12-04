#find out tickets with wins, add the wins by 2**n, find # of tickets if tickets wins multiply
import re

with open("AOC4.txt") as file:
	mylist = file.read().splitlines()	#open file with splitlines, shorter then before

numbers=[]
for i in mylist:						#extract all numbers with this funky regex
	numbers.append(re.findall(r"\d+",i))

res=[]
res1=[]
tickets = [1]*len(mylist)
for a,i in enumerate(numbers):			#check for wins, log wins per ticket, multiply by amount of tickets
	for k in range(10):
		if i[k+1] in i[11:]:			#+1 beacause ticket number is also in number[i]
			res1.append(i[k+1])
	for l in range(len(res1)):
		tickets[a+1+l] +=1*tickets[a]
		pass
	res.append(res1)
	res1=[]

num = 0									#number of wins
for i in res:
	if len(i) > 0:
		num += 2**(len(i)-1)
	else:
		pass

print("Teil 1: "+str(num))
print("Teil 2: "+str(sum(tickets)))
