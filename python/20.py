class Solution:
    def isValid(self, s: str) -> bool:
        bracketStack = []
        closeBracketMap = {
            ")": "(",
            "}": "{",
            "]": "[",
        }

        for bracket in s:
            if bracket in closeBracketMap:
                if len(bracketStack) == 0:
                    return False
                
                if bracketStack[-1] != closeBracketMap[bracket]:
                    return False
                
                bracketStack.pop()
            else:
                bracketStack.append(bracket)
        
        return len(bracketStack) == 0

# leetcode example
assert Solution().isValid("()") == True
assert Solution().isValid("()[]{}") == True
assert Solution().isValid("(]") == False
assert Solution().isValid("([)]") == False
assert Solution().isValid("{[]}") == True