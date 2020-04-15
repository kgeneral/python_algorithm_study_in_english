class Solution:
    def climbStairs(self, n: int) -> int:
        cache = {}
        return self.climb(n, cache)
    
    def climb(self, n:int, cache) -> int:
        if n in cache:
            return cache[n]
            
        if n<0:
            return 0
        if n==0:
            return 1
        
        nGoes1 = self.climb(n-1,cache)
        nGoes2 = self.climb(n-2,cache)
        
        cache[n-1] = nGoes1
        cache[n-2] = nGoes2
        
        return nGoes1 + nGoes2
