from typing import List
import math

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        start = 0
        mx = -math.inf
        for i in range(n):
            if nums[i] == 0 and i >= start:
                subMx = self.calc(nums, start, i-1)
                # print("SubMx", subMx)
                mx = max(mx, subMx, 0)
                start = i+1
        if start < n:
            # no 0 in nums
            if nums[start] == 0:
                start += 1
            subMx = self.calc(nums, start, n-1)
            # print("submx", subMx)
            mx = max(mx, subMx)
        print(mx)
        return mx


    """
    Calculate the max in range [i, j]
    """ 
    def calc(self, nums, i, j):
        # print("segment ->", nums[i:j+1])
        if j == i:
            return nums[i]
        if j < i:
            return -math.inf

        mx = nums[i]
        total = 1
        for k in range(i, j+1):
            total *= nums[k]

        if total > 0:
            return total

        # segment has odd number of negatives
        p = 1
        for k in range(i, j+1):
            if nums[k] < 0:
                if k > i:
                    mx = max(mx, p)
                
                withoutNeg = total // (p*nums[k])
                mx = max(mx, withoutNeg)
                break
            p *= nums[k]
        
        p = 1
        for k in range(j, i-1, -1):
            if nums[k] < 0:
                if k < j:
                    mx = max(mx, p)
                
                withoutNeg = total // (p*nums[k])
                mx = max(mx, withoutNeg)
                break
            p *= nums[k]
        return mx

Solution().maxProduct([2,3,-2,4])
Solution().maxProduct([-2,0,-1])
Solution().maxProduct([1, 2, -2, 3, -1, 4, -2])
Solution().maxProduct([1, -2, 0, 4, 4, -2, 1])
Solution().maxProduct([-4,-3])
Solution().maxProduct([0,2])
Solution().maxProduct([0])