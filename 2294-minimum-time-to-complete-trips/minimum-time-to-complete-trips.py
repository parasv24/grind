class Solution:
    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        lo = 1
        hi = 100000000000000
        ans = -1
        while lo <= hi:
            mid = (lo + hi) // 2
            k = 0
            flag = False
            for el in time:
                k += mid // el
                if k >= totalTrips:
                    flag = True
                    break
            if flag:
                ans = mid
                hi = mid -1
            else:
                lo = mid + 1
        return ans
        