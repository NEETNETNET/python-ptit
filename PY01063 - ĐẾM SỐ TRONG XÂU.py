for _ in range(int(input())):
    s = input()
    n = input()
    l, chiso, cnt = len(n), s.find(n), 0
    while chiso != -1:
        cnt += 1
        chiso = s.find(n, chiso + l)
    print(cnt)