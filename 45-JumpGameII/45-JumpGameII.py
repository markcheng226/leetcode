class Solution:
    def jump(self, nums: List[int]) -> int:
        l,r,res = 0,0,0

        while r<len(nums)-1:
            farest = 0
            for i in range(l,r+1):
                farest = max(farest,nums[i]+i)
            l = r
            r = farest
            res +=1
        return res