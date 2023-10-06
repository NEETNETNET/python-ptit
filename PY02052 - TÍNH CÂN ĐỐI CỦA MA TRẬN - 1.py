n = int(input())
m = [[]] * n
for i in range(n):
    m[i] = [int(j) for j in input().split()]
k = int(input())
s1,s2 = 0,0
for i in range(n):
    for j in range(n):
        if j < i:
            s1 += m[i][j]
        elif j > i:
            s2 += m[i][j] 
if abs(s1 - s2) <= k:
    print("YES")
else:
    print("NO")
print(abs(s1-s2))