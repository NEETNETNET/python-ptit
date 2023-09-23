from math import sqrt
for _ in range(int(input())):
    n = int(input())
    s = '1'
    for i in range(2,int(sqrt(n))+1):
        cnt = 0
        while n%i == 0:
            cnt +=1
            n//=i
        if cnt!= 0:
            s += ' * ' + str(i) + '^' + str(cnt)
    if n != 1:
        s += ' * ' + str(n) + '^' + '1'
    print(s)