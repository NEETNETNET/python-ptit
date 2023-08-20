import math 
def isPrime(n):
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return n > 1

n = int(input())
a = [int(i) for i in input().split()]
cnt = {}
for i in a:
	if isPrime(i):
		if i not in cnt:
			cnt[i] = 1
		else:
			cnt[i]+=1
for i in cnt:
	print(i,cnt[i])