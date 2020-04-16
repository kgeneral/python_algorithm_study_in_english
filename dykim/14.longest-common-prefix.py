class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ""
        
        result = ""
        minLen = min([len(s) for s in strs])
        
        for i in range(0, minLen):
            verticalChars = set([s[i] for s in strs])
            if len(verticalChars) == 1:
                result += verticalChars.pop()
            else:
                break
        
        return result
