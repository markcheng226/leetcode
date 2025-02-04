class Solution:
    def minimumHealth(self, damage: List[int], armor: int) -> int:
        totalDamage = sum(damage)
        highestDamage = max(damage)
        highestPrevent = min(highestDamage,armor)
        return totalDamage - highestPrevent +1