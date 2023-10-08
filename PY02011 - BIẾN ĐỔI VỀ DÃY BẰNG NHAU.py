n = int(input())
a = list(map(int,input().split()))
res = 10**9
ans  = 0
for i in a:
	plus = 0 
	for j in a:
		plus += abs(i-j)
	if plus < res:
		res = plus 
		ans = i
print(res,ans)


