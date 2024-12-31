class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        def helper(num):
            if num < 0 :
                return 1000000001
            if num == 0:
                return 0
            if num == 2 or num == 3:
                return 1
            return 1 + min(helper(num - 2), helper(num - 3))
        dp = [-1] * 100001
        dp[0] = 0
        dp[1] = 100000
        dp[2], dp[3] = 1,1
        for i in range(4, 100001):
            dp[i] = 1 + min(dp[i-2], dp[i-3])
        mp = Counter(tasks)
        ans = 0
        for key, val in mp.items():
            if dp[val] >= 100000:
                return -1
            else:
                ans += dp[val]
        return ans



        