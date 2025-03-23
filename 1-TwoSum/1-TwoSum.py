# Last updated: 3/23/2025, 5:21:34 PM
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in hashmap:
                return [i,hashmap[diff]]
            hashmap[nums[i]] = i