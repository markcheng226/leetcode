# Last updated: 7/5/2025, 9:57:06 PM
class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        n = len(cardPoints)
        total = sum(cardPoints)

        if n == k:
            return total

        window_sum = sum(cardPoints[:n-k])
        min_sum = window_sum

        for i in range(n-k,n): 
            window_sum += cardPoints[i] - cardPoints[i-(n-k)]
            min_sum = min(window_sum,min_sum)
        
        return total - min_sum
