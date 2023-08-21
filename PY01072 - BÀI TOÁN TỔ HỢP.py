def Try(i,s):
	global n, k
	if len(s) == k:
		print(*s)
		return
	for j in range(i,n):
		Try(j+1,s+[a[j]])

n,k = map(int,input().split())
a = sorted(list({int(i) for i in input().split()}))
n = len(a)
Try(0,[])