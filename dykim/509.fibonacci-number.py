class Solution:
    def fib(self, N: int) -> int:
        self.cache = {0:0, 1:1}
        return self.f(N)
    
    def f(self, n: int) -> int:
        if n in self.cache:
            return self.cache[n]
        
        fibm1 = self.f(n-1)
        fibm2 = self.f(n-2)
        self.cache[n-1]=fibm1
        self.cache[n-2]=fibm2
        
        return fibm1 + fibm2
        
