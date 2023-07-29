t = int(input())
def check(s):
    for i in range(len(s) - 1):
        if s[i] > s[i+1]: return "NO"
    return "YES"
for i in range(t):
    s = input()
    print(check(s))
