class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        nums.sort()
        cur = 0
        res = 0

        for num in nums:
            num -= cur
            if num >0 :
                cur += num
                res +=1
        return res