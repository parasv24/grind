class Solution:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        m = len(nums2)
        dp = [[0] * m for _ in range(n)]
        
        dp[n-1][m-1] = int(nums1[n-1] == nums2[m-1])
        
        for i in range(m-2, -1,-1):
            dp[n-1][i] = max(dp[n-1][i+1], int(nums1[n-1] == nums2[i]))
                
                
        for i in range(n-2, -1, -1):
            dp[i][m-1] = max(dp[i+1][m-1], int(nums1[i] == nums2[m-1]))

        for i in range(n-2, -1, -1):
            for j in range(m-2, -1, -1):
                if nums1[i] == nums2[j]:
                    dp[i][j] = 1 + dp[i + 1][ j + 1]
                else:
                    dp[i][j] = max(dp[i + 1][ j], dp[i][ j + 1])
        # x = f(0, 0)
        print(dp)
        return dp[0][0]