class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        ans = [-1 for _ in range(amount + 1)]
        ans[0] = 0
        for coin in coins:
            if coin <= amount:
                ans[coin] = 1
        
        for i in range(1, amount + 1):
            if ans[i] == -1:
                mini = 100000
                for coin in coins:
                    if i - coin > 0 and ans[i-coin] > 0:
                        mini = min(mini, ans[i - coin])
                if mini != 100000:
                    ans[i] = 1 + mini
        return ans[amount]

        