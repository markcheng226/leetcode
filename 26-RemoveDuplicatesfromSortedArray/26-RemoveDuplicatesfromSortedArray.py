# Last updated: 7/9/2025, 10:45:47 PM
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        slow = 1

        for i in range(1,len(nums)):
            if nums[i] != nums[i-1]:
                nums[slow] = nums[i]
                slow +=1
        return slow