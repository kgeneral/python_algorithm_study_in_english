# https://leetcode.com/explore/interview/card/microsoft/30/array-and-strings/187/
# elapsed time : 3 min
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        n = len(s)
        for i in range(int(n/2)):
            temp = s[n-1-i]
            s[n-1-i]=s[i]
            s[i]=temp
