# https://leetcode.com/explore/interview/card/microsoft/48/others/208/
# elapsed time : 3 min
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        cnt = collections.Counter(nums)
        return cnt.most_common()[-1][0]
