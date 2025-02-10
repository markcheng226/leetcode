class Solution:
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
        data = sorted(zip(timestamp,username,website))
        users = defaultdict(list)

        for i,user,site in data:
            users[user].append(site)
        
        patterns = Counter()

        for user,sites in users.items():
            patterns.update(set(combinations(sites,3)))
        
        return min(patterns,key = lambda x:(-patterns[x],x))
