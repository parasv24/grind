class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        stk = [prices[-1]]
        for i in range(len(prices) - 2, -1, -1):
            # print(stk)
            while len(stk) > 0 and stk[-1] > prices[i]:
                stk.pop()
            val = prices[i]
            if len(stk) > 0:
                prices[i] -= stk[-1]
            stk.append(val)
        return prices