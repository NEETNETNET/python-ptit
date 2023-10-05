from collections import Counter
s = input()
a = []
b = []
for i in range(0,len(s) + 1,2):
	s1 = s[i:i+2]
	if len(s1) < 2:
		break
	if s1 not in b:
		b.append(s1)
	a.append(s1)
cnt = Counter(a)
for i in b:
	print(i,cnt[i])
