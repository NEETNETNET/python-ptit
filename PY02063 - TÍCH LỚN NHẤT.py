n = int(input())
a = [int(i) for i in input().split()]
a.sort()
q,w,e,r,t,y = a[-1]*a[-2],a[0]*a[1],a[-1]*a[-2]*a[-3],a[0]*a[1]*a[2],a[0]*a[1]*a[-1],a[0]*a[-1]*a[-2]
print(max(max(w,max(e,max(r,max(t,y)))),q))