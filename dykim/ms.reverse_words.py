# https://leetcode.com/explore/interview/card/microsoft/30/array-and-strings/166/
# elapsed time : 8 min
class Solution:
    def reverseWords(self, s: str) -> str:
        s = re.sub('\s+', ' ', s).strip().split()
        n = len(s)
        for i in range(int(n/2)):
            temp = s[i]
            s[i] = s[n-1-i]
            s[n-1-i] = temp
        return " ".join(s)
