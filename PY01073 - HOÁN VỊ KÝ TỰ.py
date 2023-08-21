def Try(s):
	global n,check
	if len(s) == n:
		print(s)
	for i in range(n):
		if check[i] == 0:
			check[i] = 1
			Try(s+a[i])
			check[i] = 0


a = input()
n = len(a)
check = [0] * n
Try("")