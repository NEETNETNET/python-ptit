from math import gcd 
class phanSo:
	def __init__(self,x,y):
		self.x = x
		self.y = y
	def tinh(self):
		a = gcd(self.x,self.y)
		tu,mau = int(self.x/a),int(self.y/a)
		return str(tu) + '/' + str(mau)
x,y = [int(i) for i in input().split()]
p = phanSo(x,y)
print(p.tinh())