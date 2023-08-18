def check(s):
	s = str(s)
	if s != s[::-1]:
		return 0
	if len(s) % 2 == 1: 
		return 0
	a = [0,2,4,6,8]
	for i in s:
		if int(i) not in a:
			return 0
	return 1
for _ in range(int(input())):
	s = int(input())
	for i in range(s):
		if check(i):
			print(i,end=' ')
	print()
