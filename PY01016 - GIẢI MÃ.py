t = int(input())
for _ in range(t):
    s = input()
    for i in range(len(s)-1):
        if i%2 == 0: print(s[i]*int(s[i+1]),end='')
    print()