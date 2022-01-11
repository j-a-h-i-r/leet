from typing import List

class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k <= 1:
            return 0
        l = 0
        tc = 0
        prod = 1

        for i, num in enumerate(nums):
            prod *= num

            while prod >= k:
                prod //= nums[l]
                l += 1
            tc += (i-l+1)
        # print(tc)
        return tc


Solution().numSubarrayProductLessThanK([10,5,2,6], 100)
Solution().numSubarrayProductLessThanK([2, 2, 2, 5], 5)
Solution().numSubarrayProductLessThanK([5,5,5], 5)
Solution().numSubarrayProductLessThanK([1,2,3], 1)
Solution().numSubarrayProductLessThanK([1,2,3], 0)
Solution().numSubarrayProductLessThanK([57,44,92,28,66,60,37,33,52,38,29,76,8,75,22], 18)
