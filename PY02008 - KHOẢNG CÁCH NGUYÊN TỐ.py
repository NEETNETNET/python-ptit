from math import sqrt 
def prime(s):
	for i in range(2,int(sqrt(s))+1):
		if s % i == 0:
			return False
	return s > 1
pri = [0]
i = 2
while len(pri) <= 1001:
	if prime(i):
		pri.append(i)
	i +=1
n,x = map(int,input().split())
for i in range(n+1):
	x += pri[i]
	print(x,end = ' ')