def check(s):
    for i in s:
        if i > '3' or i < '0': return "NO"
    return "YES"
test = int(input())
for i in range(test):
    s = input()
    print(check(s))