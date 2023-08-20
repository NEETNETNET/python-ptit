for _ in range(int(input())):
	a,b,c = [int(i) for i in input().split()]
	a1 = [int(i) for i in input().split()]
	b1 = [int(i) for i in input().split()]
	c1 = [int(i) for i in input().split()]
	ok,i,j,k = 1,0,0,0
	while i < a and j < b and k < c:
		if a1[i] == b1[j] == c1[k]:
			ok = 0
			print(a1[i],end = ' ')
			i+=1
			j+=1
			k+=1
		elif a1[i] < b1[j]:
			i += 1
		elif b1[j] < c1[k]:
			j += 1
		else:
			k += 1
	if ok:
		print("NO") 
	print()