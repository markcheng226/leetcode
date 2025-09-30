# Last updated: 9/30/2025, 2:38:55 AM
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        low = float('inf')

        for i in range(len(prices)):
            low = min(low,prices[i])
            profit = max(profit,prices[i]-low)
        return profit

