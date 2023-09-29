for _ in range(int(input())):
	s = input()
	plus = 0
	s1 = []
	for i in s:
		if i >= '0' and i <= '9':
			plus += int(i)
		else:
			s1.append(i)
	s1.sort()
	print(*s1,sep='',end = '')
	print(plus)
