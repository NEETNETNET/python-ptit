t = int(input())
def check(s):
    a = s[::-1]
    for i in range(1,len(s)):
        if abs(ord(s[i])-ord(s[i-1])) != abs(ord(a[i])-ord(a[i-1])): return "NO"
    return "YES"
for _ in range(t):
    s = input()
    print(check(s))
