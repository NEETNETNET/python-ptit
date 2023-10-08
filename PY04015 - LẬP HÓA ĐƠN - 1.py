class Bill:
	def __init__(self,id,name,last,current):
		self.id = 'KH{:02}'.format(id)
		self.name = name
		self.total = current - last
		if self.total <= 50:
			self.total *= 100 * 1.02
		elif self.total <=100:
			self.total = 50 * 100 + (self.total - 50) * 150
			self.total *= 1.03
		else:
			self.total = 50 * 100 + 50 * 150 + (self.total - 100) * 200
			self.total *= 1.05
	def __str__(self):
		return '{} {} {}'.format(self.id,self.name,round(self.total))
a = []
for i in range(int(input())):
	name = input()
	last = int(input())
	current = int(input())
	a.append(Bill(i+1,name,last,current))
a.sort(key = lambda x : -x.total)
print(*a,sep = '\n')