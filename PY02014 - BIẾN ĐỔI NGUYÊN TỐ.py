a = [0] * 10001
b = []
for i in range(2,10001):
	if a[i] == 0:
		for j in range(i*i,10001,i):
			a[j] = 1
		b.append(i)
n = int(input())
c = list(map(int,input().split()))
ans = 0
for i in c:
	res = 10**9
	for j in b:
		res = min(res,abs(i-j))
	ans = max(res,ans)
print(ans)