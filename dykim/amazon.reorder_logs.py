# https://leetcode.com/explore/interview/card/amazon/76/array-and-strings/2974/
# elapsed time : 21 min
class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        letLogs = []
        digLogs = []
        
        for l in logs:
            log = l.split(" ", 1)
            if ord(log[1][0]) >= ord("0") and ord(log[1][0]) <= ord("9"):
                digLogs.append(l) 
            else: letLogs.append([log[1],log[0]])
                
        sortedLetLogs = [" ".join([l[1], l[0]]) for l in sorted(letLogs)]
        
        return sortedLetLogs + digLogs
