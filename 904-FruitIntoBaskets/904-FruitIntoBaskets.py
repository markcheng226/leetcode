# Last updated: 7/8/2025, 12:51:10 AM
class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        count = defaultdict(int)
        left = 0
        res = 0

        for i in range(len(fruits)):
            count[fruits[i]] +=1

            while len(count) >2:
                count[fruits[left]]-=1
                if count[fruits[left]] == 0:
                    del count[fruits[left]]
                left +=1
            
            res = max(res,i-left+1)
        return res