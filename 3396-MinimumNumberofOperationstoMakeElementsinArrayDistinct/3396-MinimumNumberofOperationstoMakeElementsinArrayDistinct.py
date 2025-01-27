from collections import Counter

class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        operations = 0
        while True:
            current_length = len(nums)
            unique_length = len(set(nums))
            if (current_length != unique_length) and nums:
                operations += 1
                nums = nums[3:]
                continue
            break
        return operations