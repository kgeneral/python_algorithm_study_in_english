# https://leetcode.com/explore/interview/card/amazon/76/array-and-strings/2964/
# elapsed time : ?
class Solution:
    def intToRoman(self, num: int) -> str:
        
        roman = ""
        
        thousands = int(num / 1000)
        num -= thousands * 1000
        hundreds = int(num / 100)
        num -= hundreds * 100
        tens = int(num / 10)
        ones = num % 10
        
        print(thousands, hundreds, tens, ones)
        
        roman += "".join(["M" for i in range(thousands)])
        roman += "".join(["C" for i in range(hundreds)]).replace("C"*9, "CM").replace("C"*5, "D").replace("C"*4, "CD")
        roman += "".join(["X" for i in range(tens)]).replace("X"*9, "XC").replace("X"*5, "L").replace("X"*4, "XL")
        roman += "".join(["I" for i in range(ones)]).replace("I"*9, "IX").replace("I"*5, "V").replace("I"*4, "IV")

        return roman
        
