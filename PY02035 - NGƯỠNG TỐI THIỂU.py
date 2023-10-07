from collections import Counter
s = input()
n = int(input())
a = []
for i in range(0,len(s),2):
	s1 = s[i:i+2]
	if len(s1) == 2:
		s1 = int(s1)
		a.append(s1)
a.sort()
cnt = Counter(a)
ok = 1
for i in cnt:
	if cnt[i] >= n:
		print(i,cnt[i])
		ok = 0
if ok:
	print("NOT FOUND") 
