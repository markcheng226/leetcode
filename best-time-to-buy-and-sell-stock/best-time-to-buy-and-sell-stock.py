class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        low = float("inf")
        res = 0

        for i in range(len(prices)):
            low = min(low,prices[i])
            res = max(res,prices[i]-low)
        return res
        