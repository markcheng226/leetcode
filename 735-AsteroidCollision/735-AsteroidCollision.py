class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        res = []
        stack = []

        for a in asteroids:
            while stack and a<0<stack[-1]:
                diff = a + stack[-1]
                if diff > 0:
                    a = 0
                elif diff < 0:
                    stack.pop()
                else:
                    a = 0
                    stack.pop()
            if a:
                stack.append(a)
        return stack