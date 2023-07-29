from math import gcd
from math import sqrt

def prime(n):
    if n < 2: return False
    for i in range(2,int(sqrt(n))+1):
        if n%i == 0: return False   
    return True

test = int(input())
for i in range(test):
    k = 0
    n = int(input())
    for i in range(n):
        if gcd(n,i) == 1: k=k+1
    if(prime(k)): print("YES")
    else: print("NO")
