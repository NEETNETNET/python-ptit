while 1:
	n = int(input())
	if n == 0:
		break
	maxi = 0
	mini = 1e10
	for _ in range(n):
		x = int(input())
		if x > maxi: 
			maxi = x
		if x < mini:
			mini = x
	if maxi == mini:
		print("BANG NHAU")
	else:
		print(mini,maxi)

