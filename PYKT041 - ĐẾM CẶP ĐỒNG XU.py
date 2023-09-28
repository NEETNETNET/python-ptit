n = int(input())
a,b,c,cnt = [0] * n,[0] * n,[0] * n,0
for i in range(n) :
    a[i] = input()
for i in range(n) :
    for j in range(n) :
        if a[i][j] == 'C' :
            b[i] += 1
            c[j] += 1
for i in range(n) :
    cnt += b[i] * (b[i] - 1) / 2
    cnt += c[i] * (c[i] - 1) / 2
print(int(cnt))