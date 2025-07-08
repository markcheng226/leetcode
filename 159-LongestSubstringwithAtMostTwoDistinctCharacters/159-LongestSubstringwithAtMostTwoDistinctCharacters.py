# Last updated: 7/7/2025, 11:56:06 PM
class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        left = 0
        res = 0
        count = defaultdict(int)

        for i in range(len(s)):
            count[s[i]] +=1
            
            while len(count)>2:
                count[s[left]]-=1
                if count[s[left]] == 0:
                    del count[s[left]]
                left +=1
            
            res = max(res,i-left+1)
        return res