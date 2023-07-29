from math import sqrt
def prime(s):
    if s < 2 : return False
    for i in range(2,int(sqrt(s))+1):
        if s % i == 0: return False
    return True
def check1(s):
    if prime(len(s)): return True
    return False
def check2(s):
    cnt = 0
    for i in s:
        if prime(int(i)): cnt += 1
    if cnt > len(s) - cnt: return True
    return False     
t = int(input())
for i in range(t): 
    s = input()
    if check1(s) and check2(s): print("YES")
    else: print("NO")