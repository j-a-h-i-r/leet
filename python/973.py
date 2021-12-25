from typing import List
from math import sqrt


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distList = []
        for i, point in enumerate(points):
            [x, y] = point
            dist = sqrt(x**2 + y**2)
            distList.append((dist, i))
            
        distSorted = sorted(distList, key=lambda a: a[0])
        closestPoints = [ points[point[1]] for point in distSorted[:k] ]
        return closestPoints

print(Solution().kClosest([[1,3],[-2,2]], 1))
print(Solution().kClosest([[3,3],[5,-1],[-2,4]], 2))