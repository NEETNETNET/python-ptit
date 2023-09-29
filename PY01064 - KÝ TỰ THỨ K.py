f = [0] * 30
f[1] = 1
for i in range(2,26):
	f[i] = 2*f[i-1] + 1
def div(n,k):
	mid = (f[n] + 1) / 2
	if k == mid:
		return chr(ord('A') + n - 1)
	if k > mid:
		return div(n-1,k-f[n-1] - 1)
	return div(n-1,k)
for _ in range(int(input())):
	n,k = map(int,input().split())
	print(div(n,k))