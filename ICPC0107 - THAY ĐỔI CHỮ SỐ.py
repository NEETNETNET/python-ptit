for _ in range(int(input())):
	p,q = input().split()
	nhap = input().split()
	if len(nhap) == 1:
		s1 = nhap[0]
		s2 = input()
	else:
		s1, s2 = nhap
	tong1 = int(s1.replace(p, q)) + int(s2.replace(p, q))
	tong2 = int(s1.replace(q, p)) + int(s2.replace(q, p))
	print(min(tong1,tong2),max(tong1,tong2))


