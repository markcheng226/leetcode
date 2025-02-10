class Solution:
    def rob(self, nums: List[int]) -> int:
        rob1,rob2 = 0,0
        for i in range(len(nums)):
            rob3 = max(rob1 + nums[i],rob2)
            rob1 = rob2
            rob2 = rob3
        return rob2