# https://leetcode.com/explore/interview/card/amazon/76/array-and-strings/2970/
# elapsed time : 30 min (-)
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        output = {}
        for word in strs:
            h = ",".join(self.hashCount(word))
            if h not in output:
                output[h] = [word]
            else:
                output[h].append(word)
                
        return output.values()
    
    def hashCount(self, word):
        counts = [0] * 26
        for c in word:
            counts[ord(c) - ord('a')] += 1
        return str(counts)
