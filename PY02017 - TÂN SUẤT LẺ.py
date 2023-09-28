from collections import Counter
for _ in range(int(input())):
    n = input()
    a = [int(i) for i in input().split()]
    cnt = Counter(a)
    for i in a:
        if cnt[i] % 2 == 1:
            print(i)
            break
