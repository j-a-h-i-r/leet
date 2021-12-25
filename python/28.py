class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle) == 0:
            return 0

        if len(haystack) == 0:
            return -1

        needleLen = len(needle)
        needleIdx = 0

        hayLen = len(haystack)
        hayIdx = 0
        
        while hayIdx < hayLen:
            if haystack[hayIdx] == needle[needleIdx]:
                needleIdx += 1
            else:
                hayIdx = hayIdx - needleIdx + 1
                needleIdx = 0

                if (hayLen - hayIdx) < needleLen:
                    return -1
            
            if needleIdx == needleLen:
                return hayIdx - needleLen + 1

            hayIdx += 1
        
        return -1

# leetcode example

print(Solution().strStr("mississippi", "issip"))

assert Solution().strStr("hello", "ll") == 2
assert Solution().strStr("aaaaa", "bba") == -1
assert Solution().strStr("", "") == 0
