class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def can_ship(cap):
            ans = 1
            cur = cap
            for el in weights:
                if el <= cur:
                    cur -= el
                else:
                    if cap >= el:
                        cur = cap - el
                        ans += 1
                    else:
                        ans += ((el - 1) // 2)  + 1
                        # print(ans)
                        cur = cap
                        ans += 1
            return ans <= days

        lo, hi = min(weights), sum(weights)
        ans = -1
        while lo <= hi:
            mid = (lo + hi) // 2
            # print(lo, mid, hi)
            if can_ship(mid):
                ans = mid
                hi = mid - 1
            else:
                lo = mid + 1
        return ans


        