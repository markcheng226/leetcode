# Last updated: 10/13/2025, 10:25:07 PM
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = [0] * 26
        res = 0
        left = 0
        max_count = 0

        for i in range(len(s)):
            index = ord(s[i])-65
            count[index] +=1
            max_count = max(max_count, count[index])

            while i-left+1 - max_count > k:
                count[ord(s[left])-65] -=1
                left +=1
            res = max(res,i-left+1)
        return res