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
        # def rec(n):
        #     if n == 1:
        #         return "1"
            
        #     small_ans = rec(n-1)
        #     return rle(small_ans)
        # return rec(n)
        cur  = "1"
        n -= 1
        while n > 0:
            ans = []
            i = 0
            while i < len(cur):
                ch = cur[i]
                cnt = 0
                while i < len(cur) and cur[i] == ch:
                    i += 1
                    cnt += 1
                ans.append(str(cnt))
                ans.append(ch)
            cur = "".join(ans)
            n -= 1 
        return cur
            

        