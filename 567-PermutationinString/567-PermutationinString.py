# Last updated: 10/26/2025, 7:32:19 PM
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n, m = len(s1), len(s2)
        if n > m:
            return False

        def idx(c): return ord(c) - 97

        need = [0] * 26
        win = [0] * 26
        for c in s1:
            need[idx(c)] += 1

        for i in range(n):
            win[idx(s2[i])] += 1
        if win == need:
            return True

        for r in range(n, m):
            win[idx(s2[r])] += 1
            win[idx(s2[r - n])] -= 1
            if win == need:
                return True
        return False
