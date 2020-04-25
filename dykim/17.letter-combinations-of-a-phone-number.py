# backtracking
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        length = len(digits)
        alphabetKey = ['abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']
        chars = [alphabetKey[int(d) - 2] for d in digits]
        self.combSet = set()
        self.backtracking("", chars)
        return list(self.combSet)
    
    def backtracking(self, comb, chars):
        if len(chars) == 0:
            if len(comb) != 0:
                self.combSet.add(comb)
            return
        
        for c in chars[0]:
            self.backtracking(comb + c, chars[1:])
