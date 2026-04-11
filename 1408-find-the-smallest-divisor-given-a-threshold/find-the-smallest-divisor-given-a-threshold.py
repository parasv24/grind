class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        l , r = 1, max(nums)
        while l <= r:
            mid = (l+r) // 2
            div_result = 0
            for el in nums:
                div_result += (el - 1) // mid + 1
            if div_result <= threshold:
                r = mid - 1
            else:
                l = mid + 1
        return l

        