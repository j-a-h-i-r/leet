from typing import List
import math

class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        
        """
        Pass 1:
        Count number of live neighbors for each cell. Use -ve values to store the count in the cell if the cell is currently dead. Use +ve otherwise.

        There's 1 edge case. If a cell is currently alive (1) but has no live neighbor then it's cell will store 0 in this case. Ideally this should be a +0. But there's no +0/-0 in python. So, we'll store a large +ve but impossible integer here to indicate that this cell is alive. Any +ve integer greater than 8 would work in this case.
        """

        m = len(board)
        n = len(board[0])

        moves = [-1, 0, 1]

        for i in range(m):
            for j in range(n):

                liveNeighbors = 0
                for di in moves:
                    for dj in moves:
                        if di == 0 and dj == 0:
                            continue

                        ni = i + di
                        nj = j + dj

                        if 0<=ni<m and 0<=nj<n:
                            if board[ni][nj] > 0:
                                liveNeighbors += 1
                
                if board[i][j] == 1:
                    board[i][j] = liveNeighbors if liveNeighbors > 0 else 9
                else:
                    board[i][j] = -liveNeighbors

        # print(board) 

        """
        Pass 2:
        The absolute values contain the count of live neighbors around the cell.
        If the value is +ve then apply rules for live cells. Else apply rule for dead cells.

        To adjust for the edge case in the previous step, if any cell has an impossible integer we'll simply count it as 0 to adjust for the edge case.
        """

        for i in range(m):
            for j in range(n):
                nCount = abs(board[i][j])
                if nCount == 9:
                    nCount == 0

                if board[i][j] > 0:
                    if 2<=nCount<=3:
                        board[i][j] = 1
                    else:
                        board[i][j] = 0
                else:
                    if nCount == 3:
                        board[i][j] = 1
                    else:
                        board[i][j] = 0
        print(board)




Solution().gameOfLife([[0,1,0],[0,0,1],[1,1,1],[0,0,0]])
Solution().gameOfLife([[1,1],[1,0]])
Solution().gameOfLife([[0, 0], [0, 0]])
Solution().gameOfLife([[0, 0, 0], [0, 1, 0], [0, 0, 0]])
Solution().gameOfLife([[1, 0, 1], [0, 1, 0], [0, 1, 0]])
Solution().gameOfLife([[1, 0, 1], [0, 1, 0], [0, 1, 0]])
Solution().gameOfLife([[1,0,0],[0,0,0],[1,0,1]])
Solution().gameOfLife([
    [1,0,0,0,0,1],
    [0,0,0,1,1,0],
    [1,0,1,0,1,0],
    [1,0,0,0,1,0],
    [1,1,1,1,0,1],
    [0,1,1,0,1,0],
    [1,0,1,0,1,1],
    [1,0,0,1,1,1],
    [1,1,0,0,0,0]
])
