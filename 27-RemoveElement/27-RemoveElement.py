# Last updated: 9/21/2025, 1:53:28 AM
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        slow = 0

        for fast in range(len(nums)):
            if nums[fast] != val:
                nums[slow] = nums[fast]
                slow +=1
        return slow