class Solution:
    def myPow(self, x: float, n: int) -> float:
        if x == 0 :
            return 0

        if n == 0:
            return 1

        res = 1
        power = abs(n)

        while power > 0:
            if power %2 ==1:
                res *= x
            x *= x
            power = power //2
        return res if n >=0 else 1/res