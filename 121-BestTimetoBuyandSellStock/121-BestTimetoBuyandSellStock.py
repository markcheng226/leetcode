# Last updated: 9/23/2025, 2:44:13 AM
class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        low = float("inf")
        profit = 0

        for i in range(len(prices)):
            low = min(low,prices[i])
            profit = max(profit,prices[i]-low)
        return profit
