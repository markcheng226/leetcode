class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        nums.sort()
        current = 0
        count = 0

        for num in nums:
            num -= current

            if num > 0:
                current += num
                count +=1
        return count