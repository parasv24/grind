class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        n = len(questions)
        dp = [-1 for _ in range(n)]
        # def f(i):
        #     if i >= n:
        #         return 0
        #     if dp[i] != -1:
        #         return dp[i]
        #     val, skip = questions[i]
        #     pick = val + f(i+skip+1)
        #     not_pick = f(i+1)
        #     dp[i] = max(pick, not_pick)
        #     return dp[i]
        for i in range(n-1, -1, -1):
            val, skip = questions[i]
            pick = val
            pick += dp[i+skip+1] if i + skip + 1 < n else 0
            not_pick = dp[i+1] if i + 1 < n else 0
            dp[i] = max(pick, not_pick)
        return dp[0]