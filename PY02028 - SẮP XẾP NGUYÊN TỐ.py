a = [0] * 10001
for i in range(2,10001):
	if a[i] == 0:
		for j in range(i*i,10001,i):
			a[j] = 1
n = int(input())
b = list(map(int,input().split()))
c = []
for i in b:
	if a[i] == 0:
		c.append(i)
c.sort()
for i in b:
	if a[i] == 0:
		print(c[0],end = ' ')
		c.pop(0)
	else:
		print(i,end = ' ')