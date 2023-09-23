n = int(input())
a = [int(i) for i in input().split()]
ok = 1 
for i in range(min(a),max(a)+1):
    if i not in a:
        ok = 0
        print(i)
        break
if ok:
    print(max(a) + 1)