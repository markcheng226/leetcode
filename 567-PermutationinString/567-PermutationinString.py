# Last updated: 10/26/2025, 7:33:48 PM
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n, m = len(s1), len(s2)
        if n > m:
            return False
            
        need = [0] * 26
        win = [0] * 26
        for c in s1:
            need[ord(c) - 97] += 1

        for i in range(n):
            win[ord(s2[i]) - 97] += 1
        if win == need:
            return True

        for r in range(n, m):
            win[ord(s2[r]) - 97] += 1
            win[ord(s2[r-n]) - 97] -= 1
            if win == need:
                return True
        return False
