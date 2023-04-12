class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans = 0
        j = len(prices) - 1
        mx = prices[j]
        while j >= 0:
            ans = max(ans, mx - prices[j])
            if prices[j] > mx:
                mx = prices[j]
            j -= 1
        return ans