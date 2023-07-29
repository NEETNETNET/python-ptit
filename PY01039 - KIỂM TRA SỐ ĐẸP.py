def check(n):
    a = n[0]
    b = n[1]
    if a == b: return "NO"
    if len(n) % 2 == 0:
        for i in range(2,len(n)-1,2):
            if n[i] != a: return "NO"
        for i in range(3,len(n),2):
            if n[i] != b: return "NO"
    else: 
        for i in range(2,len(n),2):
            if n[i] != a: return "NO"
        for i in range(3,len(n)-1,2):
            if n[i] != b: return "NO"
    return "YES"

test = int(input())
for i in range(test):
    n = input()
    print(check(n))