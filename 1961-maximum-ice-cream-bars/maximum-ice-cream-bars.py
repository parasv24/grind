class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        maxi = -1
        counts = defaultdict(int)
        for cost in costs:
            counts[cost] += 1
            maxi = max(maxi, cost)
        ans = 0
        for i in range(1, maxi+1):
            cnt = counts[i]
            val = i
            if val * cnt <= coins:
                ans += cnt
                coins -= (val * cnt)
            else:
                ans += (coins // val)
                coins -= (coins // val) * val
        return ans


        