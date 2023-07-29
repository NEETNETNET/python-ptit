from math import log
test = int(input())
for i in range(test):
    n,x,m = [ float(x) for x in input().split() ]
    print(int(log( m/n, 1 + x/100 )) + 1 )
