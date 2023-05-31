class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        res = [0]*26

        for i in s:
            res[ord(i)-ord("a")] +=1
        for i in t:
            res[ord(i)-ord("a")] -=1
        for i in range(len(res)):
            if res[i] != 0:
                return False
        return True
        