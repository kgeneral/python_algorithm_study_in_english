# https://leetcode.com/explore/interview/card/amazon/76/array-and-strings/2965/
# elapsed time : 33 min
class Solution:
    def romanToInt(self, s: str) -> int:
        number = 0
        roman = {
            "I":1,
            "V":5,
            "X":10,
            "L":50,
            "C":100,
            "D":500,
            "M":1000
        }
        roman5s = {
            "V":"I",
            "X":"I",
            "L":"X",
            "C":"X",
            "D":"C",
            "M":"C"
        }
        prev5 = None
        for i, x in enumerate(reversed(s)):
            if x in roman:
                if prev5 != None and x == roman5s[prev5]:
                    number -= roman[roman5s[prev5]]
                    prev5 = None
                    continue
                if x in roman5s:
                    prev5=x                
                number += roman[x]
            
            
        return number
