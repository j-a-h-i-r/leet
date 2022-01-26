from typing import List
import math

class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        candies = [1]*n
        pass1 = self.calcSum(candies, ratings)
        pass2 = self.calcSum(candies[::-1], ratings[::-1])
        print(pass2, sum(pass2))
        return sum(pass2)
        
    def calcSum(self, candies, ratings):
        n = len(ratings)

        for i in range(n):
            a = -math.inf
            b = -math.inf

            if i-1>=0 and ratings[i] > ratings[i-1]:
                a = candies[i-1] + 1
            if i+1<n and ratings[i] > ratings[i+1]:
                b = candies[i+1] + 1
            
            m = max(a, b)
            if m != -math.inf:
                candies[i] = m
        # print(candies)
        return candies




Solution().candy([1, 0, 2])
Solution().candy([1, 2, 2])
Solution().candy([0, 1, 2, 1, 0, 3])
Solution().candy([1,2,87,87,87,2,1])