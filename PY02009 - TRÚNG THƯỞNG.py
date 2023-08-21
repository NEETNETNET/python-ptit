for _ in range(int(input())):
	n = int(input())
	cnt = {}
	res1,res2 = 0,1e10
	for _ in range(n):
		x = int(input())
		if x in cnt:
			cnt[x] +=1
		else:
			cnt[x] = 1
		res1 = max(res1,cnt[x])
	for i in cnt:
		if cnt[i] == res1:
			res2 = min(res2,i)
	print(res2)