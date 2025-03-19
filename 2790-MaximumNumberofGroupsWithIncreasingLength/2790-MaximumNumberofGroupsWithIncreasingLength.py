class Solution:
    def maxIncreasingGroups(self, usageLimits: List[int]) -> int:
        usageLimits.sort()
        total = 0
        group_size = 1

        for limit in usageLimits:
            total += limit
            if total >= group_size * (group_size + 1) // 2:
                group_size += 1

        return group_size - 1
