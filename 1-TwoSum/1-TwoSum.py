# Last updated: 10/9/2025, 11:11:20 PM
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}

        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in hashmap:
                return [hashmap[diff],i]
            else:
                hashmap[nums[i]] = i