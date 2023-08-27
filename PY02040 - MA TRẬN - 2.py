n = int(input())
a = [[]] * n
for i in range(n):
	a[i] = [int(j) for j in input().split()]
k = int(input())
tong1,tong2 = 0,0
for i in range(n):
	for j in range(n):
		if i < n - 1 - j: 
			tong1 +=a[i][j] 
		elif i > n - 1 - j:
			tong2 += a[i][j]
if abs(tong1 - tong2) <= k:
	print("YES")
else:
	print("NO")
print(abs(tong1 - tong2))