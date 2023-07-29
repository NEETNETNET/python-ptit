t = int(input())
for i in range(t):
    a = int(input())
    s = 0
    k = 1 
    if a % 2 == 0: k = 2
    for i in range(k,a+1,2):
        s += 1/i
    print("{:.6f}".format(s))
