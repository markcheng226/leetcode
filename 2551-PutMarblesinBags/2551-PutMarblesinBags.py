# Last updated: 4/2/2025, 10:06:28 AM
class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        if k == 1:
            return 0

        n = len(weights)

        pair_cost = [ weights[i] + weights[i+1] for i in range(n-1)]

        pair_cost.sort()

        max_cost = sum(pair_cost[-(k-1):])

        min_cost = sum(pair_cost[:k-1])

        return max_cost-min_cost