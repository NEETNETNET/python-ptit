n = int(input())
b,a = [float(i) for i in input().split()],[]
maxi,mini = max(b),min(b)
for i in b:
	if i!= maxi and i!= mini:
		a.append(i)
print("{:.2f}".format(sum(a)/len(a)))