from math import sqrt

class Point:
	def __init__(self,x,y):
		self.x = x
		self.y = y
	def distance(self,l):
		x1 = self.x - l.x
		x2 = self.y - l.y
		return sqrt(x1*x1 + x2*x2)
class Triangle:
	def __init__(self,p1,p2,p3):
		self.p1 = p1
		self.p2 = p2
		self.p3 = p3
	def area(self):
		a = self.p1.distance(self.p2)
		b = self.p2.distance(self.p3)
		c = self.p3.distance(self.p1)
		if a + b <= c or abs(a-b) >= c:
			print("INVALID")
		else:
			print('{:.2f}'.format(sqrt((a + b + c) * (a + b - c) * (a - b + c) * (-a + b + c)) / 4))
n = int(input())
a = []
for _ in range(n):
	a += list(map(float,input().split()))
i = 0
for _ in range(n):
	t = Triangle(Point(a[i],a[i+1]),Point(a[i+2],a[i+3]),Point(a[i+4],a[i+5]))
	t.area()
	i+=6



