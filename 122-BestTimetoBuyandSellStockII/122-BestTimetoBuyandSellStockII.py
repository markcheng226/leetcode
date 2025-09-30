# Last updated: 9/30/2025, 3:01:13 AM
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0

        for i in range(1,len(prices)):
            if prices[i] > prices[i-1]:
                profit += prices[i] - prices[i-1]
        
        return profit
