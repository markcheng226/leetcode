# Last updated: 10/24/2025, 11:37:05 PM
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group = defaultdict(list)
        
        for s in strs:
            count= [0] * 26
            for c in s:
                count[ord(c)-ord("a")] +=1
            group[tuple(count)].append(s)
        return list(group.values())
        