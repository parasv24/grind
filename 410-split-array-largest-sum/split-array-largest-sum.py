class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        def can_split(num):
            ans = 1
            cur = 0
            for el in nums:
                if cur + el > num:
                    cur = el
                    ans += 1
                else:
                    cur += el
            return ans <= k
        lo, hi = max(nums), sum(nums)
        ans = -1
        while lo <= hi:
            mid = (lo + hi) // 2
            if can_split(mid):
                ans = mid
                hi = mid - 1
            else:
                lo = mid + 1
        return ans
        