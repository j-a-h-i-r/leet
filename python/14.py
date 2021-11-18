from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        firstString = strs[0]
        longestPrefix = ""

        for i in range(len(firstString)):
            if not all([ i < len(s) and s[i] == firstString[i] for s in strs]):
                return longestPrefix
            longestPrefix += firstString[i]
        return longestPrefix

# leetcode example
assert Solution().longestCommonPrefix(["flower","flow","flight"]) == "fl"
assert Solution().longestCommonPrefix(["dog","racecar","car"]) == ""
