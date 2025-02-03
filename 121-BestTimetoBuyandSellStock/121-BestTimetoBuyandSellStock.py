class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        low = float("inf")
        for i in range(len(prices)):
            low = min(low,prices[i])
            profit = max(profit,prices[i]-low)
        return profit