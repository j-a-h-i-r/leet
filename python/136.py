from typing import List
from functools import reduce
from unittest import TestCase

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        return reduce(lambda x, y: x ^ y, nums)


test = TestCase().assertEqual

test(Solution().singleNumber([2,2,1]), 1)
test(Solution().singleNumber([4,1,2,1,2]), 4)
test(Solution().singleNumber([1]), 1)
