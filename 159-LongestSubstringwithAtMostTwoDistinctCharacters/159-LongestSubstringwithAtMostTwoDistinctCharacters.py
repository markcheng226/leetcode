# Last updated: 7/8/2025, 12:18:20 AM
class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        count = defaultdict(int)
        left = 0
        res = 0

        for i in range(len(s)):
            count[s[i]] +=1

            while len(count) > 2:
                count[s[left]]-=1
                if count[s[left]] == 0:
                    del count[s[left]]
                left +=1
            
            res = max(res,i-left+1)
        return res