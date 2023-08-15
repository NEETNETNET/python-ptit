from math import sqrt
def nt(s):
	if s < 2: 
		return 0
	for i in range(2,int(sqrt(s)) + 1):
		if s % i == 0: 
			return 0
	return 1
def check(s):
	for i in range(1,len(s),2):
		if int(s[i]) % 2 == 0: 
			return "NO"
	for i in range(0,len(s),2):
		if int(s[i]) % 2 != 0: 
			return "NO"
	tong = 0
	for i in s:
		tong += int(i)
	if(nt(tong) == 0): 
		return "NO"
	return "YES"
for i in range(int(input())):
	print(check(input()))