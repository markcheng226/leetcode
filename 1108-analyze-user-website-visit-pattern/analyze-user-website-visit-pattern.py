from collections import defaultdict
from itertools import combinations

class Solution:
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> str:
    
        G = defaultdict(list)
        for (time, user, web) in sorted(zip(timestamp, username, website)):
            G[user].append(web)
        
        scores = defaultdict(int)
        for user, websites in G.items():
            for pattern in set(combinations(websites, 3)):
                scores[pattern] += 1
     
        max_pattern, max_cnt = '', 0
        for pattern, cnt in scores.items():
            if cnt > max_cnt or (cnt == max_cnt and pattern < max_pattern):
                max_pattern = pattern
                max_cnt = cnt
        
        return max_pattern
