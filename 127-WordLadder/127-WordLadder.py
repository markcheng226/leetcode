// Last updated: 3/21/2025, 7:58:38 PM
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        words = set(wordList)
        res = 0
        q = deque([beginWord])

        if beginWord == endWord or endWord not in wordList:
            return 0
        
        while q :
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
                            words.remove(nei)
                            q.append(nei)
        return 0
        
