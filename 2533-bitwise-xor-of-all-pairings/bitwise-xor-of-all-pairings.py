class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        m = len(nums2)
        ans = 0
        if n % 2 != 0:
            for el in nums2:
                ans ^= el
        if m % 2 != 0:
            for el in nums1:
                ans ^= el
        return ans
        