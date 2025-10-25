# Last updated: 10/24/2025, 8:58:51 PM
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count = {}

        if len(s) != len(t):
            return False

        for i in t:
            count[i] = count.get(i,0) + 1

        for i in s:
            if i not in count:
                return False
            else:
                count[i] -=1
            
            if count[i] < 0:
                return False

        return True
        
