class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        vals = [str(i) for i in range(0, 256)]
        ans = []
        def rec(i, arr):
            if i == len(s) and len(arr) == 4:
                ans.append(".".join(arr))
            p = ""
            for j in range(i, len(s)):
                p += s[j]
                if p not in vals:
                    break
                if len(arr) < 4:
                    rec(j+1, arr + [p])
                else:
                    break
        rec(0, [])
        return ans
                


        