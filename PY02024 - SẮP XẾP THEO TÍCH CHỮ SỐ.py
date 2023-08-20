def nhan(s):
	tich = 1
	for i in s:
		tich *= int(i)
	return tich 
for _ in range(int(input())):
	s = int(input())
	a = input().split()
	a.sort(key=lambda s: (nhan(s), int(s)))
	print(*a)