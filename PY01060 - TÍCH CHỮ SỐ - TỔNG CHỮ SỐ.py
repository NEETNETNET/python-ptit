def tinhTong(s):
	tong = 0
	for i in range(1,len(s),2):
		tong += int(s[i])
	return tong
def tinhTich(s):
	ok,tich = 1,1
	for i in range(0,len(s),2):
		if s[i] != '0': 
			ok = 0
			tich *= int(s[i])
	if ok:
		return 0
	return tich
for _ in range(int(input())):
	s = input()
	print(tinhTich(s),end = ' ')
	print(tinhTong(s))
