# Last updated: 9/30/2025, 3:15:16 AM
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        goal = len(nums)-1
        
        for i in range(len(nums)-2,-1,-1):
            if i + nums[i] >= goal:
                goal = i
        return True if goal == 0 else False