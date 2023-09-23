for _ in range(int(input())):
    n = int(input())
    a = [int(i) for i in input().split()]
    res,st = [0]*n,[]
    for i in range(n):
        while len(st) != 0 and a[st[-1]] <= a[i]:
            st.pop()
        res[i] = i +1 if len(st) == 0 else i - st[-1]
        st.append(i)
    print(*res)

