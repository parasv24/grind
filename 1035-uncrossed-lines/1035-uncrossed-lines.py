class Solution:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        m = len(nums2)
        dp = [[-1] * m for _ in range(n)]

        def f(i, j):
            if i >= n or j >= m:
                return 0
            if dp[i][j] != -1:
                return dp[i][j]
            if nums1[i] == nums2[j]:
                dp[i][j] = 1 + f(i + 1, j + 1)
            else:
                dp[i][j] = max(f(i + 1, j), f(i, j + 1))
            return dp[i][j]

        x = f(0, 0)
        return x