for _ in range(int(input())):
	n = int(input())
	a = input().split()
	s = {}
	ok = 1
	for i in a:
		if i in s:
			s[i] += 1
		else:
			s[i] = 1
	for i in s:
		if s[i] >= int(n/2) + 1:
			ok = 0
			print(i)
			break
	if ok: 
		print("NO") 
