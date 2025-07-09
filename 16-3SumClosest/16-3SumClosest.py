# Last updated: 7/9/2025, 1:22:31 AM
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        closest = float('inf')

        for i in range(len(nums)):
            l = i+1
            r = len(nums)-1
            while l < r:
                total = nums[i] + nums[l] + nums[r]



                if total > target:
                    r -=1
                elif total < target:
                    l +=1
                else:
                    return target
                if abs(total-target) < abs(closest - target):
                    closest = total
                
        return closest
