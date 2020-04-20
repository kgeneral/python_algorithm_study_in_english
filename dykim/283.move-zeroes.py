class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        zeros = 0
        idx = 0
        while idx < len(nums):
            if nums[idx] == 0:
                del nums[idx]
                zeros += 1
            else:
                idx += 1
        
        for i in range(zeros):
            nums.append(0)
