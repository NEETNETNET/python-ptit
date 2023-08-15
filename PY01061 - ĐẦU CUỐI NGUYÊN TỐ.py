import math
def isPrime(n):
	if n < 2: 
		return 0
	for i in range(2, int(math.sqrt(n)) + 1):
		if n % i == 0:
			return 0
	return 1

def check(s):
	tong1,tong2  = 0,0
	for i in range(len(s) - 3,len(s)):
		tong1  = tong1*10 + int(s[i])
	if isPrime(tong1) == 0: 
		return "NO"
	for i in range(0,3):
		tong2  = tong2*10 + int(s[i])
	if isPrime(tong2) == 0: 
		return "NO"
	return "YES"
for i in range(int(input())):
	print(check(input()))