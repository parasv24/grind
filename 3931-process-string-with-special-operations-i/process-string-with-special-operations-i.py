class Solution:
    def processStr(self, s: str) -> str:
        ans = []
        for ch in s:
            if ch == "*":
                if len(ans) > 0:
                    ans.pop()
            elif ch == "#":
                ans += ans
            elif ch == "%":
                ans = ans[::-1]
            else:
                ans.append(ch)
        return "".join(ans)
        