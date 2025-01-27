class Solution:
    def minimumOperations(self, nums: List[int]) -> int:

        res =0 
        while True:
            if len(nums) != len(set(nums)) and nums:
                nums = nums[3:]
                res +=1
                continue
            break
        return res