# Last updated: 10/26/2025, 4:52:10 PM
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        low = float("inf")

        for i in range(len(prices)):
            low = min(low,prices[i])
            res = max(res,prices[i]-low)
        return res