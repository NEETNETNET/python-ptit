from math import sqrt 
def prime(s):
	for i in range(2,int(sqrt(s))+1):
		if s % i == 0:
			return False
	return s > 1
def check(s):
	if prime(int(s)) == 0:
		return "No"
	s1 = s[::-1]
	if prime(int(s1)) == 0:
		return "No"
	tong = sum(int(i) for i in s)
	if prime(tong) == 0:
		return "No"
	for i in s:
		if prime(int(i)) == 0:
			return "No"
	return "Yes"
for _ in range(int(input())):
	s = input()
	print(check(s))