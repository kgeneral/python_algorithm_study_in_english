# https://leetcode.com/explore/interview/card/amazon/76/array-and-strings/2972/
# elapsed time : 8 min
class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0: return False
        stack = []
        opened = {
            "(":")",
            "{":"}",
            "[":"]"
        }
        
        for c in s:
            if c in opened:
                stack.append(c)
                continue
            else: 
                if len(stack) == 0: return False   
                curOpened = stack.pop()
                if opened[curOpened] != c:
                    return False
                
        if len(stack) > 0: return False        
        return True
