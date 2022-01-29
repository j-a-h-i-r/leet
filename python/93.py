from typing import List

class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        if len(s) > 12:
            return []
        self.valid = []
        self.f([], s)
        # print(self.valid)
        return self.valid

    def f(self, segments, s):
        if len(segments) == 3:
            lastChunk = s[segments[-1]:]
            if self.isValidChunk(lastChunk):
                self.valid.append(
                    self.putDot(segments, s)
                )
            return
        
        start = 0 if len(segments) == 0 else segments[-1]
        i = 1
        while i <= 3 and start + i < len(s):
            end = start + i
            chunk = s[start:end]
            if self.isValidChunk(chunk):
                self.f(segments + [end], s)
            else:
                break
            i += 1

    def isValidChunk(self, chunk):
        if chunk == "0":
            return True
        if chunk[0] == "0":
            return False
        if int(chunk) <= 255:
            return True
        return False

    def putDot(self, segments, s):
        chunks = []
        start = 0
        for i in segments:
            chunks.append(s[start:i])
            start = i
        chunks.append(s[start:])
        return ".".join(chunks)


Solution().restoreIpAddresses("25525511135")
Solution().restoreIpAddresses("0000")
Solution().restoreIpAddresses("000012121")
Solution().restoreIpAddresses("123456789123456789")