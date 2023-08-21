while 1:
	a = input()
	if a == '0':
		break
	k,s = a.split()
	k = int(k)
	s1 = ""
	p = "ABCDEFGHIJKLMNOPQRSTUVWXYZ_."
	for i in s:
		j = p.find(i)
		s1+=p[(j+k)%28]
	print(s1[::-1])