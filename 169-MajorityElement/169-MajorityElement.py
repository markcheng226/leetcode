# Last updated: 9/23/2025, 2:10:18 AM
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        target, count = 0,0
        for i in range(len(nums)):
            if count == 0:
                target = nums[i]
                count = 1
            elif target != nums[i]:
                count -=1
            else:
                count +=1
        return target