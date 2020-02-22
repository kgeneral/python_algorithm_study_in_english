# https://leetcode.com/explore/interview/card/amazon/76/array-and-strings/480/
# elapsed time : 30 min
class Solution:
    def firstUniqChar(self, s: str) -> int:
        counter = {}
        for i, c in enumerate(s):
            if c not in counter:
                counter[c] = [i]
            else:
                counter[c] += [i]
                
        for i, v in counter.items():
            if len(v) == 1:
                return v[0]
            
        return -1
