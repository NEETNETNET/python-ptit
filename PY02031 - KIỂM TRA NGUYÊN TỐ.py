from math import sqrt 
def isPrime(s):
	if s < 2 :
		return 0
	for i in range(2,int(sqrt(s))+1):
		if s % i == 0:
			return 0
	return 1
n,m = [int(i) for i in input().split()]
for i in range(n):
	a  = [isPrime(int(j)) for j in input().split()]
	print(*a)