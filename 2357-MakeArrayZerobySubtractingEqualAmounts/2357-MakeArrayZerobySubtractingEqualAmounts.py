class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        nums.sort()
        current =0
        res = 0

        for num in nums:
            num -= current

            if num >0:
                current += num
                res +=1
        return res