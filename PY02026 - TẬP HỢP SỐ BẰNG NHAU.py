n,m = map(int,input().split())
a = [int(i) for i in input().split()]
b = [int(i) for i in input().split()]
a1 = list(set(a))
b1 = list(set(b))
a1.sort()
b1.sort()
if a1 == b1:
	print("YES")
else:
	print("NO")