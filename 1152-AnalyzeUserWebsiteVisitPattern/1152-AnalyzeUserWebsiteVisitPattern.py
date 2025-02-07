class Solution:
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
        
        G = defaultdict(list)
        for time, user, website in sorted(zip(timestamp, username, website)):
            G[user].append(website)
        

        scores = defaultdict(int)
        for users, websites in G.items():
            size = len(websites)
            pattern = set()
            

            for i in range(size-2):
                for j in range(i+1, size-1):
                    for k in range(j+1,size):
                        curr_pattern = (websites[i], websites[j], websites[k])
                        if curr_pattern not in pattern:
                            pattern.add(curr_pattern)
                            scores[curr_pattern] +=1
        
        
        max_pattern, max_score = '', 0
        for pattern, count in scores.items():
            if count > max_score or (count == max_score and pattern < max_pattern):
                max_pattern = pattern
                max_score = count
        
        return max_pattern