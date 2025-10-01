# Last updated: 9/30/2025, 8:43:31 PM
class Solution:
    def jump(self, nums: List[int]) -> int:
        res= 0
        cur_end = 0
        farest =0

        for i in range(len(nums)-1):
            farest = max(farest,i+nums[i])
            if i == cur_end:
                res +=1
                cur_end = farest
                if cur_end >= len(nums)-1:
                    break
        return res
