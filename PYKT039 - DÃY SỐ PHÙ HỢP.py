def check(a,b):
    for i in range(len(a)):
        if a[i] > b[i]:
            return "NO"
    return "YES"
for _ in range(int(input())):
    n = input()
    a = [int(i) for i in input().split()]
    b = [int(i) for i in input().split()]
    a = sorted(a)
    b = sorted(b)
    print(check(a,b))