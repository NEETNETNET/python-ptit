while 1:
	a = [int(i) for i in input().split()]
	if a.count(0) == 4:
		break
	cnt = 0
	while a.count(a[0]) != 4:
		cnt += 1
		res = a[0]
		for i in range(4):
			if i == 3: 
				a[i] = abs(a[i] - res)
			else:
				a[i] = abs(a[i] - a[i+1])
	print(cnt)