# Last updated: 9/23/2025, 2:24:50 AM
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        slow = 1 

        for fast in range(1,len(nums)):
            if nums[fast] != nums[slow-1]:
                nums[slow] = nums[fast]
                slow +=1
        return slow


