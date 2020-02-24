# https://leetcode.com/explore/interview/card/amazon/80/dynamic-programming/489/
# TODO : reduce TC
class Solution:
    def longestPalindrome(self, s: str) -> str:
        if self.isPalindrome(s): return s
        n = len(s)
        leftWise = self.longestPalindrome(s[1:])
        rightWise = self.longestPalindrome(s[:n-1])
        return leftWise if len(leftWise) > len(rightWise) else rightWise
    
    def isPalindrome(self, s):
        n = len(s)
        for i in range(int(n/2)):
            if s[i] != s[n-1-i]:
                return False
        return True
            
