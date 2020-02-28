# https://leetcode.com/explore/interview/card/microsoft/30/array-and-strings/162/
# elapsed time : 6 min
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = re.sub('[^a-zA-Z0-9]', '', s) .lower()
        n = len(s)
        for i in range(int(n/2)):
            if s[i] != s[n-1-i]:
                return False
        return True
