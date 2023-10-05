def check(k):
    for i in a:
    	if i // k == i // (k+1):
    		return 0
    return 1 

def solve():
    global n, a
    n = int(input())
    a = list(map(int, input().split()))
    for i in range(min(a), 0, -1):
        if check(i):
            ans = 0
            for j in a:
                ans += j // (i + 1) + 1
            print(ans)
            return
solve()