def gt(s):
	if s == 0 :
		return 1
	return s * gt(s-1)

for _ in range(int(input())):
	s = input()
	tong = sum(gt(int(i)) for i in s)
	if tong == int(s):
		print("Yes")
	else:
		print("No")