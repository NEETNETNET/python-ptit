import math
def isPrime(n):
	if n < 2: 
		return 0
	for i in range(2, int(math.sqrt(n)) + 1):
		if n % i == 0:
			return 0
	return 1

def check(s):
	tong  = 0
	for i in range(len(s) - 4,len(s)):
		tong  = tong*10 + int(s[i])
	if isPrime(tong): 
		return "YES"
	return "NO"
for i in range(int(input())):
	print(check(input()))