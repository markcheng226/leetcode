class Solution:
    def minimumOperations(self, nums: List[int]) -> int:

        res = 0
        while True:
            if (len(nums) != len(set(nums)) and nums):
                res +=1
                nums = nums[3:]
                continue
            break
        return res
