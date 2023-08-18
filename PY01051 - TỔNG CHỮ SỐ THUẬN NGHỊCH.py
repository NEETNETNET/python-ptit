def check(s):
	if len(s) <=1 or s != s[::-1]: 
		return "NO"
	return "YES"
t = int(input())
for _ in range(t):
    s = input()
    tong = sum(int(i) for i in s)
    print(check(str(tong)))
