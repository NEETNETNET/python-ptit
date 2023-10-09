from math import sqrt 
def nt(s):
	for i in range(2,int(sqrt(s))+1):
		if s%i == 0:
			return False
	return s > 1
n,m = map(int,input().split())
a = [[0]] * n 
ans = -1
for i in range(n):
	a[i] = list(map(int,input().split()))
	for j in a[i]:
		if nt(j) and j > ans:
			ans = j
if ans == -1:
	print("NOT FOUND")
else:
	print(ans)
	for i in range(n):
		for j in range(m):
			if a[i][j] == ans:
				print('Vi tri [{}][{}]'.format(i,j))
