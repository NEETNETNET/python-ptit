def check(s):
	s1 = str(s)
	if len(s1) < 2:
		return False
	return s1 == s1[::-1]
n,m = map(int,input().split())
a = [[0]] * n 
ans = -1
for i in range(n):
	a[i] = list(map(int,input().split()))
	for j in a[i]:
		if check(j) and j > ans:
			ans = j
if ans == -1:
	print("NOT FOUND")
else:
	print(ans)
	for i in range(n):
		for j in range(m):
			if a[i][j] == ans:
				print('Vi tri [{}][{}]'.format(i,j))
