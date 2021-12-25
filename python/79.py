from unittest import TestCase
from typing import List
from collections import deque

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)
        cols = len(board[0])

        for r in range(rows):
            for c in range(cols):
                if board[r][c] == word[0]:
                    visited = [[False]*cols for x in range(rows)]
                    exists = self.runBfs(board, visited, r, c, 0, word)
                    if exists:
                        return True
        return False

    
    def runBfs(self, board: List[List[str]], visited, r, c, matchedLen, word: str) -> bool:
        wordLen = len(word) - 1
        rows = len(board)
        cols = len(board[0])

        if visited[r][c] == True:
            return False
        
        if matchedLen > wordLen:
            return False

        if board[r][c] != word[matchedLen]:
            return False
        
        if matchedLen == wordLen:
            return True

        visited[r][c] = True

        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        for i, j in dirs:
            nx, ny = r+i, c+j

            if 0<=nx<rows and 0<=ny<cols:
                exist = self.runBfs(board, visited, nx, ny, matchedLen + 1, word)
                if exist:
                    return True

        visited[r][c] = False
        return False



test = TestCase().assertEqual

test(Solution().exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCCED"), True)
test(Solution().exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "FDECSE"), True)
test(Solution().exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "DEESCD"), False)
test(Solution().exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "SEE"), True)
test(Solution().exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCB"), False)
test(Solution().exist([["a"]], "a"), True)
test(Solution().exist([["a"]], "b"), False)
test(Solution().exist([["a", "a"]], "aaa"), False)
test(Solution().exist([["A","B","C","E"],["S","F","E","S"],["A","D","E","E"]], "ABCESEEEFS"), True)
