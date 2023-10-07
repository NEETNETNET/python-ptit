for _ in range(int(input())):
	n = int(input())
	a = list(map(int,input().split()))
	b = [0]*n
	c = [0]*n
	res = a[0]
	for i in range(1,n):
		b[i] = res
		res = max(res,a[i])
	res = a[-1]
	for i in range(len(a)-2,-1,-1):
		c[i] = res 
		res = min(res,a[i])
	cnt = 0
	if a[0] < c[0]:
		cnt += 1
	if a[n-1] >= b[n-1]:
		cnt +=1
	for i in range(1,len(a)-1):
		if a[i] >= b[i] and a[i] < c[i]:
			cnt +=1
	print(cnt)
