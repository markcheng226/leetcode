class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left, res, zero =0,0,0

        for right in range(len(nums)):
            if nums[right] == 0:
                zero +=1
            while zero > k:
                if nums[left] == 0:
                    zero-=1
                left +=1
            res = max(res,right-left+1)
        return res
