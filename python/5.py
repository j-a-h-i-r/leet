class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        
        mx = 1
        mxi, mxj = 0, 0

        for i in range(n):
            p1 = self.longPal(i, i, s) + 1
            p2 = 0
            if i + 1 < n and s[i] == s[i+1]:
                p2 = self.longPal(i, i+1, s) + 2
            
            if p1 > mx:
                mx = p1
                mxi = i - p1//2
                mxj = i + p1//2
            if p2 > mx:
                mx = p2
                mxi = i - (p2-2)//2
                mxj = i+1 + (p2-2)//2

        # print(mx, s[mxi:mxj+1])
        return s[mxi:mxj+1]
    
    def longPal(self, i, j, s):
        if i-1 < 0 or j+1 >= len(s):
            return 0
        
        if s[i-1] != s[j+1]:
            return 0
        
        return 2 + self.longPal(i-1, j+1, s)

        
Solution().longestPalindrome("babad")
Solution().longestPalindrome("cbbd")
Solution().longestPalindrome("safjsdakfjlkadjflksajdflkajsdfsldfksdfiyebcdcdlsasdfieurfjjjjjjjjjjaksjflsdkajfkldajfldajfkdlsajflkdajflkadsjflkdjfafjfsafdnncvxbvhakdfhrqerfsdpfdfpdsfpdsfdfdsjfkadjfadjflkdjfdsfoeyrdhfkdgfdhjgfdhjgfytfvadfdjshsafjsdakfjlkadjflksajdflkajsdfsldfksdfiyebcdcdlsasdfieurfjjjjjjjjjjaksjflsdkajfkldajfldajfkdlsajflkdajflkadsjflkdjfafjfsafdnncvxbvhakdfhrqerfsdpfdfpdsfpdsfdfdsjfkadjfadjflkdjfdsfoeyrdhfkdgfdhjgfdhjgfytfvadfdjshhsjdfdavftyfgjhdfgjhdfgdkfhdryeofsdfjdklfjdafjdakfjsdfdfsdpfsdpfdfpdsfreqrhfdkahvbxvcnndfasfjfafjdklfjsdaklfjadklfjasldkfjadlfjadlkfjakdslfjskajjjjjjjjjjfrueifdsasldcdcbeyifdskfdlsfdsjaklfdjasklfjdakljfkadsjfashsjdfdavftyfgjhdfgjhdfgdkfhdryeofsdfjdklfjdafjdakfjsdfdfsdpfsdpfdfpdsfreqrhfdkahvbxvcnndfasfjfafjdklfjsdaklfjadklfjasldkfjadlfjadlkfjakdslfjskajjjjjjjjjjfrueifdsasldcdcbeyifdskfdlsfdsjaklfdjasklfjdakljfkadsjfas")