from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = {}
        for num in nums:
            if num in seen:
                return True
            seen[num] = True
        return False


Solution().containsDuplicate([1,2,3,1])
Solution().containsDuplicate([1,2,3,4])
Solution().containsDuplicate([1,1,1,3,3,4,3,2,4,2])