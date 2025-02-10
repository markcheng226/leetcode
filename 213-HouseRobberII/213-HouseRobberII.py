class Solution:
    def rob(self, nums: List[int]) -> int:
        return max(nums[0],self.rob2(nums[1:]),self.rob2(nums[:-1]))


    def rob2(self, nums: List[int]) -> int:
        rob1,rob2 = 0,0
        for i in range(len(nums)):
            rob3 = max(nums[i]+rob1,rob2)
            rob1 = rob2
            rob2 = rob3
        return rob2
        