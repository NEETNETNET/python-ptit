class Student:
    def __init__(self,name,c,t):
        self.name = name 
        self.c = c
        self.t = t
    def __str__(self):
        return self.name + " " + str(self.c) + " " + str(self.t) + '\n'
a = []
for _ in range(int(input())):
    x = input()
    y,z = map(int,input().split())
    a.append(Student(x,y,z))
a.sort(key = lambda i : ((-1) * i.c, i.t , i.name))
print(*a)