class Solution:
    def jump(self, nums: List[int]) -> int:
        res = 0
        r = l = 0

        while r < len(nums)-1:
            far = 0
            for i in range(l,r+1):
                far = max(far,nums[i]+i)
            l = r+1
            r = far
            res +=1
        return res
