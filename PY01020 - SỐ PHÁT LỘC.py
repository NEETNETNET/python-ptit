def check(s):
    if len(s) < 2: return "NO"
    if s[-1] == '6' and s[-2] == '8': return "YES"
    return "NO"
t = int(input())
for _ in range(t):
    s = input()
    print(check(s))
