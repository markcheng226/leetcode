class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        curbuy = cursell = 0
        nextbuy = nextsell = 0

        for i in range(len(prices)-1,-1,-1):
            curbuy = max(nextbuy,-prices[i]+nextsell)
            cursell = max(nextsell,prices[i]+nextbuy)
            nextbuy = curbuy
            nextsell = cursell
        return curbuy