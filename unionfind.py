class unionfind:
    
    def __init__(self,N):
       self.n = N
       self.par = [-1]*(N+1)
       self.size = [1]*(N+1)
       
    def root(self,x):
        while self.par[x] != -1:
            x = self.par[x]
        return x
    
    def unite(self,u,v):
        rootu = self.root(u)
        rootv = self.root(v)
        if self.size[rootu] < self.size[rootv]:
            self.par[rootu] = rootv
            self.size[rootv] += self.size[rootu]
        else:
            self.par[rootv] = rootu
            self.size[rootu] += self.size[rootv]
            
    def issame(self,u,v):
        return self.root(u) == self.root(v)