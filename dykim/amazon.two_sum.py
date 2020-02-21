# https://leetcode.com/explore/interview/card/amazon/76/array-and-strings/508/
# elapsed time : around 5 min

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        numsDict = {}
        for idx, val in enumerate(nums):
            numsDict[val] = idx 
        for idx, val in enumerate(nums):
            diff = target - val
            if diff in numsDict:
                if idx == numsDict[diff]: continue
                return [idx, numsDict[diff]]
