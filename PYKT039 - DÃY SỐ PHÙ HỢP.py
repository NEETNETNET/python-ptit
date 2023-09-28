def check(a,b):
    for i in range(len(a)):
        if a[i] > b[i]:
            return "NO"
    return "YES"
for _ in range(int(input())):
    a,b = [],[]
    a.sort()
    b.sort()
    print(check(a,b))
