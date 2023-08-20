from math import gcd 
class phanSo:
	def __init__(self,x,y):
		self.x = x
		self.y = y
	def tinh(self,phanSo):
		tu = self.x*phanSo.y + self.y*phanSo.x 
		mau = self.y * phanSo.y
		a = gcd(tu,mau)
		tu,mau = int(tu/a),int(mau/a)
		return str(tu) + '/' + str(mau)
x,y,a,b = [int(i) for i in input().split()]
p1 = phanSo(x,y)
p2 = phanSo(a,b)
print(p1.tinh(p2))