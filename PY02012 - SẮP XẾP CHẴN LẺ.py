n = int(input())
a, b, c= [], [], []
while True :
    x = [int(x) for x in input().split()]
    a += x
    if len(a) == n: 
        break
for i in a:
    if i % 2 == 1 :
        b.append(i)
    else: 
        c.append(i)
b = sorted(b)
c = sorted(c, key = lambda x : -x)
for i in a:
    if i%2 == 1 :
        print(b[-1], end = " ")
        b.pop()
    else :
        print(c[-1], end = " ")
        c.pop()