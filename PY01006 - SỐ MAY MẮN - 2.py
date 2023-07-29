def lucky(n):
    for i in n:
        if i != '4' and i != '7': return "NO"
    return "YES"
test = int(input())
for i in range(test):
    n = input()
    print(lucky(n))

