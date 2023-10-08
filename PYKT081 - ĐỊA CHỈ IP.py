def check(s):
	if len(s) < 4:
		return "NO"
	for i in s:
		if i.isdigit():
			if int(i) < 0 or int(i) > 255:
				return "NO"
		else:
			return "NO"
	return "YES"
for _ in range(int(input())):
	s = input().split('.')
	print(check(s))
