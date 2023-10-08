from math import sqrt 
def nt(s):
	for i in range(2,int(sqrt(s))+1):
		if s % i == 0:
			return False
	return s > 1

n = int(input())
a = list(map(int,input().split()))
b = []

for i in a:
	if i not in b:
		b.append(i)
n = len(b)

for i in range(1,n):
	b[i] += b[i-1]

ok = 1
for i in range(n):
	if nt(b[i]) and nt(b[-1] - b[i]):
		ok = 0
		print(i)
		break
		
if ok:
	print("NOT FOUND")

