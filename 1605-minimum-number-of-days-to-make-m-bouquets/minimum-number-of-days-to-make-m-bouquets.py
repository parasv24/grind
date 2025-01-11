class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        if m * k > len(bloomDay):
            return -1
        def is_possible(day):
            arr = [1 if el <= day else 0 for el in bloomDay]
            ans = 0
            cur = 0
            for el in arr:
                if el == 1:
                    cur += 1
                else:
                    cur = 0
                if cur == k:
                    ans += 1
                    cur = 0
            return ans >= m
        lo, hi = min(bloomDay), max(bloomDay)
        ans = -1
        while lo <= hi:
            mid = (lo + hi) // 2
            if is_possible(mid):
                ans = mid
                hi = mid - 1
            else:
                lo = mid + 1
        return ans


        