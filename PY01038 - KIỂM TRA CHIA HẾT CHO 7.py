t = int(input())
for i in range(t):
    n = input()
    while int(n) % 7 != 0:
        n1 = str(n)[::-1]
        n = int(n) + int (n1)
        n = str(n)
    print(n)
                
