class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        @cache
        def rec(i, curr):
            if curr == amount:
                return 1
            if i >= len(coins) or curr > amount:
                return 0
            ans = 0
            ans +=rec(i, curr + coins[i])
            ans += rec(i+1, curr)
            return ans
        return rec(0, 0)
            