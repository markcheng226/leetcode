class Solution:
    def minimumHealth(self, damage: List[int], armor: int) -> int:
        total = sum(damage)
        highest_damage = max(damage)
        highest_prevent = min (highest_damage,armor)
        return total-highest_prevent +1