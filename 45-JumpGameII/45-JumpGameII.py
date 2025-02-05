class Solution:
    def jump(self, nums: List[int]) -> int:
        l =r = 0
        res =0

        while r < len(nums)-1:
            far = 0
            for i in range(l,r+1):
                far = max(far,nums[i]+i)
            l = r
            r= far
            res +=1

        return res
