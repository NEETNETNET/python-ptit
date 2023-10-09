n,m = map(int,input().split())
a = map(int,input().split())
cnt = {}
Max = 0
for i in a:
	if i in cnt:
		cnt[i]+=1
	else:
		cnt[i] = 1
	Max = max(Max,cnt[i])
res,ans = 0,0
for i in range(m+1):
	if i in cnt and cnt[i] > res and cnt[i] != Max:
		ans = i
		res = cnt[i]
if ans == 0:
	print("NONE")
else:
	print(ans) 