# Last updated: 10/8/2025, 9:15:51 PM
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        need = Counter(ransomNote)
        have = Counter(magazine)

        for c in need:
            if need[c] > have[c]:
                return False
        return True