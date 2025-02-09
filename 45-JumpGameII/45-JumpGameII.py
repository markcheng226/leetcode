class Solution:
    def jump(self, nums: List[int]) -> int:
        l=r=0
        res =0

        while r< len(nums)-1:
            farest = 0
            for i in range(l,r+1):
                farest = max(farest,nums[i]+i)
            l = r+1
            r = farest
            res +=1
        return res
