class Student:
	def __init__(self,name,birth,marks):
		self.name = name
		self.birth = birth
		self.score = sum(marks)
	def __str__(self):
		return f'{self.name} {self.birth} {self.score}'

name = input()
birth = input()
marks = [float(i) for i in input().split()]
print(Student(name,birth,marks))