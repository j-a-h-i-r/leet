from typing import List
import math
from collections import deque

class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        d = {}
        for w in wordList:
            d[w] = math.inf
        
        if endWord not in d:
            print([])
            return []
        
        ans = self.bfs(beginWord, endWord, d)
        print(ans)
        return ans
        
    def bfs(self, s, e, words):
        q = deque()
        q.append((s, 0, [s]))
        words[s] = True
        foundLevel = math.inf
        paths = []
        while q:
            # print(q)
            cw, l, path = q.popleft()
            for w in words:
                if l < words[w] and self.adjacent(cw, w):
                    if w == e:
                        p = path + [w]
                        paths.append(p[:])
                        foundLevel = l
                    # else:
                    words[w] = l + 1

                    if l <= foundLevel:
                        q.append((w, l+1, path + [w]))
        return paths
    
    def adjacent(self, w1, w2):
        changeCount = 0
        for i in range(len(w1)):
            if w1[i] != w2[i]:
                changeCount += 1
        return changeCount == 1

Solution().findLadders("hit", "cog", ["hot","dot","dog","lot","log","cog"])
Solution().findLadders("abc", "def", ["abf", "aef", "def", "aec"])
Solution().findLadders("abc", "def", ["abf", "dbc", "dbf", "aef", "def", "aec"])
Solution().findLadders("hit", "cog", ["hot","dot","dog","lot","log"])
