from typing import List

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        self.gen(n, k, 1, [], res)
        # print(res)
        return res

    def gen(self, n, k, last, comb, res):
        if len(comb) == k:
            res.append(comb[:])
            return
        
        for num in range(last, n+1):
            comb.append(num)
            self.gen(n, k, num+1, comb, res)
            comb.pop()
        
Solution().combine(4, 2)
Solution().combine(1, 1)
Solution().combine(20, 8)
