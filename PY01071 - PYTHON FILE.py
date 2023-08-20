def check(s):
	if s[-3:] != ".py" or len(s) < 3:
		return "no" 
	return "yes"
s = input().lower()
print(check(s),end='')
