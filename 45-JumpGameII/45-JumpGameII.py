# Last updated: 9/30/2025, 4:06:59 AM
class Solution:
    def jump(self, nums: List[int]) -> int:
        far,end,res = 0,0,0
        for i in range(len(nums)-1):
            far = max(far,nums[i]+i)
            if i == end:
                res +=1
                end = far
                if end >= len(nums)-1:
                    break
        return res