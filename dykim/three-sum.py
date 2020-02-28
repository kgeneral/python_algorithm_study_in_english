# https://leetcode.com/problems/3sum/submissions/
# from : https://leetcode.com/problems/3sum/discuss/232712/Best-Python-Solution-(Explained)
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        nums = sorted(nums)
        result = []
        for i in range(n-2):
            if nums[i] > 0: break
            if i>0 and nums[i-1]==nums[i]: continue
            l = i+1
            r = n-1
            while l < r:
                localSum = nums[i] + nums[l] + nums[r]
                #print(nums[i], nums[l], nums[r], localSum)
                #print(i, l, r)
                if localSum < 0: l+=1
                elif localSum > 0: r-=1
                else: 
                    result.append([nums[i], nums[l], nums[r]])
                    while l<r and nums[l] == nums[l+1]: l+=1
                    while l<r and nums[r] == nums[r-1]: r-=1
                    l+=1
                    r-=1
                
        return result
    
            
            
       
    
        
        
