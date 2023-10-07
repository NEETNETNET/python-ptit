s1 = [i.lower() for i in input().split()]
s2 = [i.lower() for i in input().split()]
c1,c2,c3 = {},{},{}
for i in s1:
	c1[i] = 1
	c2[i] = 1
for i in s2:
	c1[i] = 1
	c3[i] = 1
for i in sorted(c1):
	print(i,end = ' ')
print()
for i in sorted(c2):
	if i in c3:
		print(i,end = ' ')
