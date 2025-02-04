class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        words = set(wordList)
        res =0

        if (beginWord == endWord) or (endWord not in wordList):
            return 0
        
        q = deque([beginWord])
            
        while q:
            res +=1
            for i in range(len(q)):
                node = q.popleft()
                if node == endWord:
                    return res
                for i in range(len(node)):
                    for c in range(97,123):
                        if chr(c) == node[i]:
                            continue
                        nei = node[:i] + chr(c) + node[i+1:]
                        if nei in words:
                            q.append(nei)
                            words.remove(nei)
        return 0