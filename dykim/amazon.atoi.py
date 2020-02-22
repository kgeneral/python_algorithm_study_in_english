# https://leetcode.com/explore/interview/card/amazon/76/array-and-strings/2962/
# elasped time : 55 min
class Solution:
    def myAtoi(self, str: str) -> int:
        sign = 1
        valstr = ""
        numStarts = False
        digitStarts = False
        for c in str:
            if c == ' ': 
                if numStarts: break
                else: continue
                    
            if self.isSignAndDigit(c) == False: break
                
            if self.isSign(c): 
                if digitStarts:
                    break
                if numStarts:
                    valstr="0"
                    break
                else: numStarts=True
            
            if self.isDigit(c): 
                numStarts=True
                digitStarts=True
            
            valstr += c
        
        valstr = "0" if digitStarts == False else valstr
        val = 0 if valstr == "" else int(valstr)
        return min(2**31-1, val) if val >= 0 else max(-2**31, val)
    
    def isSignAndDigit(self, c):
        return self.isSign(c) or self.isDigit(c)
    
    def isSign(self, c):
        return c == '+' or c == '-'    
    
    def isDigit(self, c):
        return ord(c) >= ord('0') and ord(c) <= ord('9')
