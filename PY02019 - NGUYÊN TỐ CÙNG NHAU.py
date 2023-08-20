from math import gcd
n = int(input())
a = [int(i) for i in input().split()]
a.sort()
for i in range(len(a)-1):
	for j in range(1,len(a)):
		if gcd(a[i],a[j]) == 1 and a[i] < a[j]:
			print(a[i],a[j])

