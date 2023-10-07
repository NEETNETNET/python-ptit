n,m = map(int,input().split())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
a = list(set(a))
b = list(set(b)) 
c1,c2 = {},{}
for i in a:
	c1[i] = 1
for i in b:
	c2[i] = 1
for i in sorted(c1):
	if i in c2:
		print(i,end = ' ')
print()
for i in sorted(c1):
	if i not in c2:
		print(i,end = ' ')
print()
for i in sorted(c2):
	if i not in c1:
		print(i,end = ' ')

