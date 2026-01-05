class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxp , maxi = 0, prices[-1]
        for i in range(len(prices) - 1, -1, -1):
            if prices[i] > maxi:
                maxi = prices[i]
            maxp = max([maxp, maxi - prices[i]])
        return maxp



        