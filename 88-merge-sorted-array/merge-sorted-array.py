class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        sz = m + n
        while(sz > 0):
            if m == 0:
                nums1[sz - 1] = nums2[n-1]
                n-= 1
                sz -= 1
                continue
            if n == 0:
                nums1[sz-1] = nums1[m - 1]
                m -= 1
                sz -= 1
                continue
            if nums1[m - 1] > nums2[n-1]:
                nums1[sz-1] = nums1[m - 1]
                m -= 1
            else:
                nums1[sz - 1] = nums2[n-1]
                n-= 1
            sz -= 1
        