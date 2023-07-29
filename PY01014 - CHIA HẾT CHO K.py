a,k,n = [int(x) for x in input().split()]
i = 1
ok = 1
while k*i <=n:
    if k*i - a > 0 :
        ok = 0
        print(k*i - a,end = ' ')
    i+=1 
if ok: print(-1)
