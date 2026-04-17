class Solution:
    def countAndSay(self, n: int) -> str:
        def rle(s):
            if len(s) == 0:
                return ""
            
            cur = s[0]
            i = 0
            while i < len(s) and s[i] == cur:
                i += 1
            return f"{i}{cur}" + rle(s[i:])
        def rec(n):
            if n == 1:
                return "1"
            
            small_ans = rec(n-1)
            return rle(small_ans)
        return rec(n)
            

        