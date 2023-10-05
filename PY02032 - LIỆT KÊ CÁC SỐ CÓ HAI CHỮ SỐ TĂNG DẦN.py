s = input()
a = []
for i in range(0,len(s) + 1,2):
	s1 = s[i:i+2]
	if len(s1) < 2:
		break
	if s1 not in a:
		a.append(s1)
a.sort()
print(*a)	
