class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        vals = [str(i) for i in range(0, 256)]
        ans = []
        def rec(i, arr):
            if i == len(s) and len(arr) == 4:
                ans.append(".".join(arr))
            if i == len(s):
                return
            p = ""
            for j in range(i, len(s)):
                p += s[j]
                if p not in vals:
                    break
                rec(j+1, arr + [p])
        rec(0, [])
        return ans
                


        