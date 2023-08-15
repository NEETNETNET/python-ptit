n = int(input())
for i in range(n):
	a = input()
	tich = 1
	for j in a:
		if j != '0':
		 tich *= int(j)
	print(tich)