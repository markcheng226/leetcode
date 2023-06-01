class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        low = float("inf")
        
        for i in range(len(prices)):
            low = min(low,prices[i])
            res = max(res, prices[i]-low)
        return res
        