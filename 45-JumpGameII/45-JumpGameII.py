# Last updated: 9/30/2025, 3:26:00 AM
class Solution:
    def jump(self, nums: List[int]) -> int:
        res,cur_end,far = 0,0,0

        for i in range(len(nums)-1):
            far = max(far,nums[i]+i)
            if i == cur_end:
                res +=1
                cur_end = far
                if cur_end>=len(nums)-1:
                    break
        return res