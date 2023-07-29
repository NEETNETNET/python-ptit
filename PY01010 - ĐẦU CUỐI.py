def check(n):
    if(n[0]==n[-2] and n[1]==n[-1]): return "YES"
    return "NO"
test = int(input())
for i in range(test):
    s = input()
    print(check(s))

