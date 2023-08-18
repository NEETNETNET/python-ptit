from math import sqrt 
def prime(s):
	if s < 2:
		return "NO"
	for i in range(2,int(sqrt(s))+1):
		if s % i == 0: 
			return "NO"
	return "YES"
for _ in range(int(input())):
	s = input()
	tong = sum(int(i) for i in s)
	print(prime(tong))
