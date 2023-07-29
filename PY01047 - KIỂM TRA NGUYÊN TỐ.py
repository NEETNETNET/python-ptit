from math import sqrt
def prime(s):
    if s < 2 : return False
    for i in range(2,int(sqrt(s))+1):
        if s % i == 0: return False
    return True
t = int(input())
for i in range(t): 
    s = input()
    a =""
    a += s[-4] + s[-3] + s[-2] + s[-1]
    if prime(int(a)): print("YES")
    else: print("NO") 
