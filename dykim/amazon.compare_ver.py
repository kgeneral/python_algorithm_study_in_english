# https://leetcode.com/explore/interview/card/amazon/76/array-and-strings/502/
# elasped time : 18 min
class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1 = version1.split(".")
        v2 = version2.split(".")
        
        v1 = self.reduceRedundantZeros(v1)
        v2 = self.reduceRedundantZeros(v2)
        
        i = 0
        while i < min(len(v1), len(v2)):
            if int(v1[i]) > int(v2[i]):
                return 1
            elif int(v1[i]) < int(v2[i]):
                return -1
            i += 1
        
        if len(v1) == len(v2): return 0
        if len(v1) > len(v2): return 1
        if len(v1) < len(v2): return -1
    
    def reduceRedundantZeros(self, versionList):
        idx = len(versionList)-1
        while idx >= 0:
            if int(versionList[idx]) == 0:
                versionList.pop()
                idx -= 1
            else: break
        return versionList
