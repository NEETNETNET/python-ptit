class Student:
	def __init__(self,index,name,score):
		self.name = name
		self.index = 'HS{:02}'.format(index)
		self.score = round((sum(score) + score[0] + score[1]) /12 + 0.01,1)
		if self.score >= 9.0:
			self.feed = "XUAT SAC"
		elif self.score >= 8.0:
			self.feed = "GIOI"
		elif self.score >= 7.0:
			self.feed = "KHA"
		elif self.score >= 5.0:
			self.feed = "TB"
		else:
			self.feed = "YEU"
	def __str__(self):
		return '{} {} {} {}'.format(self.index,self.name,self.score ,self.feed)
a = []
for i in range(int(input())):
	name = input()
	score = list(map(float,input().split()))
	a.append(Student(i+1,name,score))
a.sort(key = lambda x : (-x.score,x.index))
print(*a,sep = '\n')

