def Try(s):	
	global check,n,cnt,a
	if len(s) == n:
		a.append(s)
		cnt +=1 
	for i in range(n,0,-1):
		if check[i] == 0:
			check[i] = 1
			Try(s+str(i))
			check[i] = 0

for _ in range(int(input())):
	n = int(input())
	check = [0]*(n+1)
	cnt = 0
	a = []
	Try("")
	print(cnt)
	print(*a)