import numpy as np

class DSU:
    def __init__(self , n):
        self.n = n
        self.par = [i for i in range(n)]
        self.sz = [1] * n
    
    def get(self, x):
        if self.par[x] == x:
            return x
        else:
            return self.get(self.par[x])
        
    def merge(self, x, y):
        x = self.get(x)
        y = self.get(y)
        if x == y:
            return False
        if self.sz[x] < self.sz[y]:
            x , y = y , x
        self.sz[x] += self.sz[y]
        self.par[y] = x
        return True
t = 15
for __ in range(t):
    n = np.random.randint(3 , 25)
    a = [np.random.randint(1 , 1001) for __ in range(n)]
    dsu = DSU(n)
    
    edges = []
    for i in range(n - 1):
        for j in range(i + 1 , n):
            flip = np.random.randint(0 , 2)
            if flip:
                edges.append([i , j])
            else:
                edges.append([j , i])
    
    np.random.shuffle(edges)
    tree = []
    for e in edges:
        if dsu.merge(e[0] , e[1]):
            tree.append([e[0] , e[1]])
    assert len(tree) == n - 1
    print(a , tree , sep = '\n')
