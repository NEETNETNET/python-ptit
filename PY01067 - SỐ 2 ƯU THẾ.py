a = ['0','1','2']
b = []
def check(s):
	cnt = 0
	for i in s:
		if i == '2':
			cnt +=1
	if len(s) - cnt < cnt: 
		return 1
	return 0 

def Try(s):
	if check(s):
		b.append(s)
	if len(s) < 10:
		for i in a:
			Try(s+i)
Try('1')
Try('2')
for _ in range(int(input())):
	n = int(input())
	b = sorted([int(i) for i in b])
	for i in range(n):
		print(b[i],end = ' ')
	print()