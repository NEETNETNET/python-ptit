class Student:
	def __init__(self,id,name,score1,score2):
		self.id = "TS0" + str(id)
		self.name = name
		if score1 > 10:
			self.score1 = score1 / 10
		else:
			self.score1 = score1
		if score2 > 10:
			self.score2 = score2 / 10
		else:
			self.score2 = score2
		self.score = (self.score1 + self.score2) / 2
		if self.score < 5:
			self.feed = "TRUOT"
		elif self.score < 8:
			self.feed = "CAN NHAC"
		elif self.score < 9.5:
			self.feed = "DAT"
		else:
			self.feed = "XUAT SAC"
a = []
for i in range(int(input())):
	name = input()
	score1 = float(input())
	score2 = float(input())
	a.append(Student(i+1,name,score1,score2))
a.sort(key = lambda x : -x.score)
for i in a:
	print(i.id,i.name,'{:.2f}'.format(i.score),i.feed)