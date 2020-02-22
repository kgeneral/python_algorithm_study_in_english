# https://leetcode.com/explore/interview/card/amazon/76/array-and-strings/2971/
# elapsed time : 15 min
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        counter = [0] * (len(nums) + 1)
        for i in nums:
            counter[i] += 1
        for idx, val in enumerate(counter):
            if val == 0:
                return idx
        
        return -1
