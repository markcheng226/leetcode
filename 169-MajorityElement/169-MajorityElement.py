# Last updated: 9/30/2025, 12:58:02 AM
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        target = 0

        for i in range(len(nums)):
            if count == 0:
                target = nums[i]
                count +=1
            
            else:
                if nums[i] == target:
                    count +=1
                else:
                    count -=1
        return target