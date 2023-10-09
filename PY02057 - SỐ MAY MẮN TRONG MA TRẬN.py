n,m = map(int,input().split())
a = [[0]] * n 
Max = 0
Min = 10**9
for i in range(n):
	a[i] = list(map(int,input().split()))
	for j in a[i]:
		if j > Max:
			Max = j
		if j < Min:
			Min = j
ans = Max - Min
k,ok = 0,0
for i in range(n):
	for j in range(m):
		if a[i][j] == ans:
			if k ==0:
				print(ans)
				ok = 1
				k = 1
			print('Vi tri [{}][{}]'.format(i,j))
if ok == 0:
	print("NOT FOUND")

			
