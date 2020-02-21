# https://leetcode.com/explore/interview/card/amazon/76/array-and-strings/508/
# elapsed time : around 5 min
# TODO : do more TC optimization

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        for i in range(n):
            for j in range(i+1,n):
                if i==j: continue
                if nums[i]+nums[j]==target: return [i,j] 
            
        return []       
