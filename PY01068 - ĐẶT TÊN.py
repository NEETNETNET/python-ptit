global n,k
def Try(j,s):
	if len(s) == k:
		print(*s)
	for i in range(j,n):
		Try(i+1,s + [a[i]])

n,k = map(int,input().split())
s = input().split()
a = []
for i in s:
	if i not in a:
		a.append(i)
a.sort()
n = len(a)
Try(0,[])