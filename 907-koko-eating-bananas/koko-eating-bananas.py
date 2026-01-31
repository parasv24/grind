class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def can_eat_bananas(num):
            ans = 0
            for el in piles:
                ans += ((el - 1) // num ) +1
            if ans <= h:
                return True
            return False
        # piles.sort()
        lo = 1
        hi = max(piles)
        ans = -1
        while lo <= hi:
            mid = (lo + hi) // 2
            if can_eat_bananas(mid):
                ans = mid
                hi = mid - 1
            else:
                lo = mid + 1
        return ans
        