import math
def isPrime(n):
	if n < 2: 
		return 0
	for i in range(2, int(math.sqrt(n)) + 1):
		if n % i == 0:
			return 0
	return 1

def check(s):
	if not isPrime(len(s)): 
		return "NO"
	cnt = 0 
	for i in s:
		if isPrime(int(i)): 
			cnt +=1
	if cnt < len(s) - cnt: 
		return "NO"
	return "YES"
for i in range(int(input())):
	print(check(input()))