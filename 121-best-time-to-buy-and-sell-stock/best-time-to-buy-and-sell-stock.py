class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        maxis  = [-1] * n
        i = n - 1
        while i >= 0:
            if i == n-1:
                maxis[i] = prices[i]
            else:
                maxis[i] = max(maxis[i+1], prices[i])
            i -= 1
        ans = 0
        for i in range(0, n):
            ans = max(ans, maxis[i] - prices[i])
        return ans

        