from collections import defaultdict
from itertools import combinations
from typing import List

class Solution:
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
        # 1. 按时间戳排序数据
        data = sorted(zip(timestamp, username, website))  # [(time, user, site)]
        
        # 2. 构建用户访问记录
        user_visits = defaultdict(list)
        for time, user, site in data:
            user_visits[user].append(site)
        
        # 3. 枚举所有模式并统计分数
        pattern_count = defaultdict(int)
        for user, sites in user_visits.items():
            # 生成用户访问记录的所有长度为 3 的组合
            patterns = set(combinations(sites, 3))  # 去重同一用户重复模式
            for pattern in patterns:
                pattern_count[pattern] += 1  # 每个模式被访问的用户数量+1
        
        # 4. 找到分数最高且字典序最小的模式
        max_pattern = max(sorted(pattern_count), key=lambda p: pattern_count[p])
        
        # 5. 返回结果
        return list(max_pattern)
