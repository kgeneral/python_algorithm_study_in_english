# https://leetcode.com/explore/interview/card/amazon/76/array-and-strings/2968/
# elapsed time : 15 min
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle) == 0: return 0
        
        idx = 0
        while idx < len(haystack) - len(needle) + 1:
            if self.compareFrom(haystack, needle, idx): return idx
            idx+=1
        
        return -1
        
    def compareFrom(self, haystack, needle, i):
        return haystack[i:i+len(needle)] == needle
            
