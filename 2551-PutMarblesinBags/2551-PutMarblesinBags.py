# Last updated: 4/3/2025, 7:37:15 PM
class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:

        if k == 1:
            return 0

        n = len(weights)

        pair_cost = [weights[i]+weights[i+1]for i in range(n-1)]

        pair_cost.sort()

        max_cost = sum(pair_cost[-(k-1):])

        min_cost = sum(pair_cost[:(k-1)])
        
        res = max_cost - min_cost

        return res