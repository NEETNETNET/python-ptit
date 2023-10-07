def check(s):
	if s[0] != '6':
		return "NO"
	for i in range(1,len(s)):
		if s[i] != '6' and s[i] != '8':
			return "NO"
		if i>=2 and s[i-2:i+1] == "888":
			return "NO"
	return "YES"
s = input()
print(check(s))