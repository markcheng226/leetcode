# Last updated: 9/30/2025, 3:14:14 AM
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        goal = len(nums)-1
        
        for i in range(len(nums)-1,-1,-1):
            if i + nums[i] >= goal:
                goal = i
        return True if goal == 0 else False