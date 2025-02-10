class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        cur = 0
        res = 0
        nums.sort()

        for num in nums:
            num -=cur

            if num > 0:
                cur +=num
                res +=1
        return res
