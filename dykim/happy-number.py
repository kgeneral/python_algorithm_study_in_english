# https://leetcode.com/problems/happy-number/submissions/
# elapsed time : 12 min
class Solution:
    def isHappy(self, n: int) -> bool:
        cache = {}
        while n > 1:
            n = self.happy(n)
            if n in cache:
                return False
            cache[n] = True
        return True
                
    def happy(self, n):
        nextN = 0
        while n >= 1:
            digit = n % 10
            n = int(n / 10)
            nextN += digit ** 2 
        return nextN
            
