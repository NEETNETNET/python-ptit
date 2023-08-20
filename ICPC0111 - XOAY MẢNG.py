for i in range(int(input())):
	n, d = [int(i) for i in input().split()]
	a = input().split()
	print(*a[-(n-d):],*a[0:-(n-d)])