class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        cnts= defaultdict(int)
        majCount = int(len(nums)/2)
        for n in nums:
            cnts[n] += 1
            if cnts[n] > majCount:
                return n
        return -1
