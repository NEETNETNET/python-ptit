for _ in range(int(input())):
	n,k = map(int,input().split())
	a = list(map(int,input().split()))
	Max = max(a)
	b,c = [],[]
	for i in range(n):
		if a[i] == Max:
			a.insert(i,k)
			break
	for i in a:
		if i < 0:
			b.append(i)
		else:
			c.append(i)
	print(*b,sep=' ',end = ' ')
	print(*c,sep = ' ')
	