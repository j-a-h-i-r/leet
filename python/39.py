from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        self.ret = []
        self.c = candidates
        self.r(0, target, [])
        return self.ret
        
    def r(self, idx, target, taken):
        # print(target, taken)
        if target < 0:
            return
        if target == 0:
            print(taken)
            self.ret.append(taken)
            return
            
        for i in range(idx, len(self.c)):
            self.r(i, target - self.c[i], taken + [self.c[i]])
            
        
Solution().combinationSum([2,3,6,7], 7)