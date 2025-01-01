class Solution:
    def maxScore(self, s: str) -> int:
        sm = sum(map(int, list(s)))
        cnt = int(s[0] == "0")
        ans = cnt + sm - ((cnt + 1) % 2)
        for i in range(1, len(s)-1):
            cnt += int(s[i]== "0")
            ans = max(ans, cnt + sm - (i + 1 - cnt))
        return ans
        