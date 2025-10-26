# Last updated: 10/26/2025, 2:23:54 PM
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}

        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in hashmap:
                return [i,hashmap[diff]]
            else:
                hashmap[nums[i]] = i