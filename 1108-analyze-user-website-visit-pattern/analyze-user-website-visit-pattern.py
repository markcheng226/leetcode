from collections import defaultdict
from itertools import combinations
from typing import List

class Solution:
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> str:
        # 1. 创建用户访问记录字典，按时间戳排序
        G = defaultdict(list)
        for (time, user, web) in sorted(zip(timestamp, username, website)):
            G[user].append(web)
        
        # 2. 统计三元组模式的出现次数
        scores = defaultdict(int)
        for user, websites in G.items():
            # 生成用户访问记录中所有长度为3的组合，并去重
            for pattern in set(combinations(websites, 3)):
                scores[pattern] += 1
        
        # 3. 找出出现次数最多的三元组模式
        max_pattern, max_cnt = '', 0
        for pattern, cnt in scores.items():
            # 更新最大模式：次数多或者次数相等但字典序更小
            if cnt > max_cnt or (cnt == max_cnt and pattern < max_pattern):
                max_pattern = pattern
                max_cnt = cnt
        
        # 4. 返回最终结果
        return max_pattern
