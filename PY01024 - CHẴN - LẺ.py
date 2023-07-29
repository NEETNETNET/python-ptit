def check1(s):
    tong = 0
    for i in s:
        tong += int(i)   
    if tong%10 == 0: return True
    return False
    
def check2(s):
    for i in range(len(s)-1):
        if abs(int(s[i])-int(s[i+1])) !=2: return False
    return True
t = int(input())
for _ in range(t):
    s = input()
    if check1(s) and check2(s): print("YES")
    else: print("NO")
