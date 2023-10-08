for j in range(int(input())):
	s1 = input()
	s2 = input()
	a,b = {},{}
	for i in s1:
		if i in a:
			a[i] +=1
		else:
			a[i] = 1
	for i in s2:
		if i in b:
			b[i] +=1
		else:
			b[i] = 1
	if a == b:
		print('Test {}: YES'.format(j+1))
	else:
		print('Test {}: NO'.format(j+1))
