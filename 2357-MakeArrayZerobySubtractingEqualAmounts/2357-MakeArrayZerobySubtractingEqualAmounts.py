class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        nums.sort()
        current = 0
        res = 0

        for i in range(len(nums)):
            nums[i] -= current
            if nums[i] > 0:

                current +=nums[i]
                res +=1
        return res