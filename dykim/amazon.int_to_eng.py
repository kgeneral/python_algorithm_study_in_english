# https://leetcode.com/explore/interview/card/amazon/76/array-and-strings/481/
# elapsed time : 50min
class Solution:
    def numberToWords(self, num: int) -> str:
        if num == 0: return "Zero"
        self.notations = {
            0:"",
            1:"One",
            2:"Two",
            3:"Three",
            4:"Four",
            5:"Five",
            6:"Six",
            7:"Seven",
            8:"Eight",
            9:"Nine",
            10:"Ten",
            11:"Eleven",
            12:"Twelve",
            13:"Thirteen",
            14:"Fourteen",
            15:"Fifteen",
            16:"Sixteen",
            17:"Seventeen",
            18:"Eighteen",
            19:"Nineteen",
            20:"Twenty",
            30:"Thirty",
            40:"Forty",
            50:"Fifty",
            60:"Sixty",
            70:"Seventy",
            80:"Eighty",
            90:"Ninety",
            100:"Hundred",
            1000:"Thousand",
            1000000:"Million",
            1000000000:"Billion"
        }
            
        billions = int(num / (1000 * 1000 * 1000))
        num -= billions * (1000 * 1000 * 1000)
        millions = int(num / (1000 * 1000))
        num -= millions * (1000 * 1000)
        thousands = int(num / (1000))
        ones = num % 1000
        
        represent = []
        if billions > 0:
            represent += [self.representUnder1000(billions), self.notations[1000000000]]
        if millions > 0:
            represent += [self.representUnder1000(millions), self.notations[1000000]]
        if thousands > 0:
            represent += [self.representUnder1000(thousands), self.notations[1000]]
        if ones > 0:
            represent += [self.representUnder1000(ones)]
                  
        
        return " ".join(represent)


    def representUnder1000(self, num):
        under100 = num % 100
        hundreds = int((num % 1000) / 100)
        represent = []
        if hundreds > 0:
            represent += [self.notations[hundreds], self.notations[100]]     
        if under100 > 0:
            represent += [self.representUnder100(under100)]
        
        return " ".join(represent)
        
    def representUnder100(self, num):
        if num < 21: return self.notations[num]
        if num % 10 == 0: return self.notations[num]
        return " ".join(
            [self.notations[int(num / 10) * 10], self.notations[num % 10]]
        ) 
