from typing import List
from unittest import TestCase

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        direction = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        m, n = len(matrix), len(matrix[0])
        r, c = 0, 0
        di = 0

        spiral = []
        steps = m * n

        rowLimit, colLimit = 0, 0
        while steps > 0:
            # print(matrix[r][c])
            spiral.append(matrix[r][c])

            dr, dc = direction[di]
            nr, nc = r+dr, c+dc

            # print(nr, nc, rowLimit, colLimit)
            if nr<rowLimit or nc<colLimit or nr+rowLimit>=m or nc+colLimit>=n:
                # print("Overstepped!")
                # Overstepped
                # Time to change direction
                di += 1
                if di == 3:
                    rowLimit += 1
                if di == 4:
                    di = 0
                    colLimit += 1

                # Correct the mistake
                dr, dc = direction[di]
                nr, nc = r+dr, c+dc

            r, c = nr, nc
            steps -= 1
        # print(spiral)
        return spiral

test = TestCase().assertEqual

test(Solution().spiralOrder([[1,2,3],[4,5,6],[7,8,9]]), [1,2,3,6,9,8,7,4,5])
test(Solution().spiralOrder([[1,2,3,4],[5,6,7,8],[9,10,11,12]]), [1,2,3,4,8,12,11,10,9,5,6,7])
test(Solution().spiralOrder([
    [1,  2, 3, 4],
    [5,  6, 7, 8],
    [9, 10,11,12],
    [13,14,15,16]
]),
    [1,2,3,4,8,12,16,15,14,13,9,5,6,7,11,10]
)
test(Solution().spiralOrder([
    [1,  2, 3, 4, 5],
    [5,  6, 7, 8, 6],
    [9, 10,11,12, 7],
    [13,14,15,16, 8],
    [11,12,13,12,11]
]),
    [1,2,3,4,5,6,7,8,11,12,13,12,11,13,9,5,6,7,8,12,16,15,14,10,11]
)
