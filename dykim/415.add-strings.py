class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        result = ""
        idx1 = len(num1) - 1
        idx2 = len(num2) - 1
        
        carriage = 0
        while max(idx1, idx2) >= 0:
            digit1 = int(num1[idx1]) if idx1 >= 0 else 0
            digit2 = int(num2[idx2]) if idx2 >= 0 else 0
            digit = digit1 + digit2 + carriage
            carriage = int(digit / 10)
            result = str(digit % 10) + result
            
            idx1 -= 1
            idx2 -= 1
        
        if carriage == 1:
            result = "1" + result
        
        return result
