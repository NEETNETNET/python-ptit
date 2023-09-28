for _ in range(int(input())) :
    n, m = [int(x) for x in input().split()]
    a = [[0]] * n
    b = [[0]] * 3
    s = 0
    for i in range(n) : 
        a[i] = [int(x) for x in input().split()]
    for i in range(3) : 
        b[i] = [int(x) for x in input().split()]
    alpha = 2
    for i in range(alpha, n) :
        for j in range(alpha, m) :
            for k in range(i-alpha,i+1):
                for l in range(j-alpha,j+1):
                    s += a[k][l] * b[k-i+alpha][l-j+alpha]
    print(s)