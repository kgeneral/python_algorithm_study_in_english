class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ""
        
        result = ""
        minLen = len(strs[0])
        for s in strs:
            minLen = min(minLen, len(s))
        
        for i in range(0, minLen):
            if len(set([s[i] for s in strs])) == 1:
                result += s[i]
            else:
                break
        
        return result
