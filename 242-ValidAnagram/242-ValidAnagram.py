# Last updated: 10/10/2025, 8:03:12 PM
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False
        
        count = {}
        for i in t:
            count[i] = count.get(i,0) +1
        
        for i in s:
            if i not in count:
                return False
            count[i] -=1

            if count[i] < 0:
                return False
        return True

