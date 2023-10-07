class Gamer:
	def __init__(self,index,name,start,finish):
		self.index = index 
		self.name = name
		self.time = finish[0] * 60 + finish[1] - start[0] * 60 - start[1]
a = []
for _ in range(int(input())):
	index = input()
	name = input()
	start = [int(i) for i in input().split(':')]
	finish = [int(i) for i in input().split(':')]
	a.append(Gamer(index,name,start,finish))
a.sort(key = lambda x : -x.time)
for i in a:
	print(i.index,i.name,i.time//60,"gio",i.time%60,"phut")
