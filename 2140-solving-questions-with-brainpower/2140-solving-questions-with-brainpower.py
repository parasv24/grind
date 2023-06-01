class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        n = len(questions)
        dp = [-1 for _ in range(n)]
        def f(i):
            if i >= n:
                return 0
            if dp[i] != -1:
                return dp[i]
            val, skip = questions[i]
            pick = val + f(i+skip+1)
            not_pick = f(i+1)
            dp[i] = max(pick, not_pick)
            return dp[i]
        return f(0)