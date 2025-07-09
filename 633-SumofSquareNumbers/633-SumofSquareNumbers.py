# Last updated: 7/8/2025, 11:53:15 PM
class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        left = 0
        right = int(math.isqrt(c))

        while left <= right:
            total = left*left + right*right
            if total > c:
                right -=1
            elif total < c:
                left +=1
            else:
                return True
        return False