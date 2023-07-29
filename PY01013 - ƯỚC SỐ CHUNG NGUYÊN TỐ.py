from math import gcd
from math import sqrt
def phan_tich(x):
    tong = 0
    while x != 0:
        tong += x%10
        x = int(x/10)
    return tong
def prime(x):
    if x < 2: return "NO"
    else:
        for i in range(2,int(sqrt(x))+1):
            if x%i == 0: return "NO"
    return "YES"
t = int(input())
for _ in range(t):
    x,y = [int(a) for a in input().split()]
    print(prime(phan_tich(gcd(x,y))))
