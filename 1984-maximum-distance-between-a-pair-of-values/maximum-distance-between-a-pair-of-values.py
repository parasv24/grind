class Solution:
    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
        i = 0
        j = 0
        ans = 0
        while i < len(nums1):
            while j < len(nums2) and nums2[j] >= nums1[i]:
                j += 1
            ans = max(j - 1 - i, ans)
            i += 1
        return ans
        