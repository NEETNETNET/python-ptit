cnt = 0 
n = int(input())
a = [int(i) for i in input().split()]
for i in range(n - 1):
	if a[i] != a[i+1]:
		cnt += 1
print(cnt)
