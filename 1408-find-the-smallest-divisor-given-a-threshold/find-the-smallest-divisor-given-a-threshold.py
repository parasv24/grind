class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        if threshold < len(nums):
            return False
        def is_possible(num):
            ans = 0
            for el in nums:
                ans += ceil(el / num)
            return ans <= threshold
        lo, hi, ans = 1, max(nums), -1
        while lo <= hi:
            mid = (lo + hi) // 2
            if is_possible(mid):
                ans = mid
                hi = mid - 1
            else:
                lo = mid + 1
        return ans
        