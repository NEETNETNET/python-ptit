fb = [1] * 93
for i in range(3,93):
	fb[i] = fb[i-1] + fb[i-2]
for _ in range(int(input())):
	a,b = map(int,input().split())
	for i in range(a,b+1):
		print(fb[i],end=' ')
	print()