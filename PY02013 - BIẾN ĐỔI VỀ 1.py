while 1:
	s = int(input())
	if s == 0:
		break
	cnt = 1
	while s != 1:
		cnt += 1
		if s % 2 == 0:
			s = s /2
		else:
			s = s*3 + 1
	print(cnt)
