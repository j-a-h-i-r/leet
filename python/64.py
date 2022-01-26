from typing import List
import math

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        self.memo = {}
        ans = self.minimize(grid, 0, 0)
        # print(ans)
        return ans
    def minimize(self, grid, i, j):
        key = f"{i}_{j}"
        if key in self.memo:
            return self.memo[key]

        m = len(grid)
        n = len(grid[0])

        if i == m-1 and j == n-1:
            return grid[m-1][n-1]
        
        if i>=m or j >= n:
            return math.inf

        ans = grid[i][j] + min(
            self.minimize(grid, i+1, j),
            self.minimize(grid, i, j+1)
        )
        self.memo[key] = ans
        return ans
        
Solution().minPathSum([[1,3,1],[1,5,1],[4,2,1]])
Solution().minPathSum([[1,2,3],[4,5,6]])
