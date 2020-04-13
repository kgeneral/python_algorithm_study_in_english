class Solution:
    def addBinary(self, a: str, b: str) -> str:
        ai = len(a) - 1
        bi = len(b) - 1
        
        result = ""
        carriage = 0
        while max(ai, bi) >= 0:
            
            aai = 0
            bbi = 0
            if ai >= 0:
                aai=int(a[ai])
            if bi >= 0:
                bbi=int(b[bi])

            localSum = aai + bbi + carriage
            carriage = 0
            
            if localSum > 1:
                localSum -= 2
                carriage = 1
                
            
            result = str(localSum) + result
            
            ai -= 1
            bi -= 1
            
        if carriage > 0:
            result = str(carriage) + result
            
        return result
            
            
        
