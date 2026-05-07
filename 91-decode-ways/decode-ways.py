class Solution:
    def numDecodings(self, s: str) -> int:
        vals = [str(i) for i in range(1, 27)]
        @cache
        def rec(i):
            if i == len(s):
                return 1
            string = ""
            ans = 0
            for j in range(i, len(s)):
                string += s[j]
                if string not in vals:
                    break
                ans += rec(j+1)
            return ans
        return rec(0)
                
