n = int(input())
a = []
while len(a) < n:
	x = list(map(int,input().split()))
	a += x
ok = 1
for i in range(1,max(a)+1):
	if i not in a:
		print(i)
		ok = 0
if ok: 
	print("Excellent!")