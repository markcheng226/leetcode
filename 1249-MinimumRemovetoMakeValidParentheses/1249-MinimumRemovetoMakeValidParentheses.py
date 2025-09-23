# Last updated: 9/23/2025, 3:41:58 AM
class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        temp = []
        open_count = 0
        for i in range(len(s)):
            ch = s[i]
            if ch == '(':
                open_count +=1
                temp.append(ch)
            elif ch == ')':
                if open_count > 0:
                    open_count -=1
                    temp.append(ch)
            else:
                temp.append(ch)
        
        res = []

        remove = open_count

        for ch in reversed(temp):
            if ch == '(' and remove > 0:
                remove -=1
            else:
                res.append(ch)
        
        return "".join(reversed(res))