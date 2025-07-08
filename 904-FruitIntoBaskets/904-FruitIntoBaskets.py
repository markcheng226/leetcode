# Last updated: 7/7/2025, 10:57:26 PM
class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        count = defaultdict(int)
        left = 0
        res = 0

        for i in range(len(fruits)):
            count[fruits[i]] +=1

            while len(count) >2:
                count[fruits[left]] -=1
                if count[fruits[left]] == 0:
                    del count[fruits[left]]
                left +=1
        
            res = max(res, i-left+1)
        return res