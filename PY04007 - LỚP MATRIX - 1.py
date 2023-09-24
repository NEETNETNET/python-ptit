class Matrix:
    def __init__(self,n,m,mtr):
        self.n = n 
        self.m = m
        self.mtr = mtr
    def mul(self):
        ans = []
        for i in range(self.n):
            ans += [[0]*self.n]
            for j in range(self.n):
                for k in range(self.m):
                    ans[i][j] += self.mtr[i][k] * self.mtr[j][k]
        return Matrix(self.n,self.n,ans)
    def __str__(self):
        for i in self.mtr:
            print(*i)
        return ''
for _ in range(int(input())):
    n,m = map(int,input().split())
    a = [0]*n
    for i in range(n):
        a[i] = [int(j) for j in input().split()]
    print(Matrix(n,m,a).mul())
