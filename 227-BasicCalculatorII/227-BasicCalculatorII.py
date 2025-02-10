class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        sign = '+'
        num = 0

        for i in range(len(s)):
            char = s[i]
            if char.isdigit():
                num = num *10 + int(char)

            if char in "+-*/" or i == len(s)-1:
                if sign == '+':
                    stack.append(num)
                elif sign == '-':
                    stack.append(-num)
                elif sign == '*':
                    stack.append(stack.pop() * num)
                elif sign == '/':
                    stack.append(int(stack.pop()  /num))
                sign = char
                num = 0
        return sum(stack)