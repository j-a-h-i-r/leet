class Solution:
    '''
    Start from the end of both strings.
    If they contain non # character then they must match. If a mismatch found in this step then they can't be equal
    Now skip the # (backspace) and the characters removed by the backspace. If we exhaust the starting index for both string in this
    step then they are a match.
    Repeat the previous steps. If one string exhaust the starting index but the other does not then they don't match
    '''
    def backspaceCompare(self, s: str, t: str) -> bool:
        i = len(s)-1
        j = len(t)-1

        skip = [0, 0]

        while i>=0 and j>=0:
            while i>=0 and j>=0 and "#" not in (s[i], t[j]):
                if s[i] != t[j]:
                    return False
                i-=1
                j-=1
            
            while i>=0 and (s[i]=="#" or skip[0]>0):
                if s[i] == "#":
                    skip[0] += 1
                else:
                    skip[0] -= 1
                i-=1
            while j>=0 and (t[j]=="#" or skip[1]>0):
                if t[j] == "#":
                    skip[1] += 1
                else:
                    skip[1] -= 1
                j-=1
            
            if i<0 and j<0:
                return True
        return False


print(Solution().backspaceCompare("ab#c", "ad#c"))
print(Solution().backspaceCompare("ab##", "c#d#"))
print(Solution().backspaceCompare("a#c", "b"))
print(Solution().backspaceCompare("a", "b"))
print(Solution().backspaceCompare("###", "#"))
print(Solution().backspaceCompare("#a#a", "#b#a#####"))
print(Solution().backspaceCompare("bcd", "abcd"))
