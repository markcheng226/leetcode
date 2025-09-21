# Last updated: 9/21/2025, 2:30:55 AM
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        slow = 2
        for fast in range(2,len(nums)):
            if nums[fast] != nums[slow-2]:
                nums[slow] = nums[fast]
                slow+=1
        return slow

        if len(nums)<2:
            return len(nums)
