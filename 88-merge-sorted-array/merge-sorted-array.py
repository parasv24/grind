class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if n ==0:
            return nums1
        sz = m + n
        m-=1
        n -=1
        sz -= 1
        while(sz >= 0):
            # print(m , n, nums1, sz)
            if m < 0 or (n >= 0 and nums1[m] <= nums2[n]):
                nums1[sz] = nums2[n]
                n -= 1
            else:
                nums1[sz] = nums1[m]
                m -= 1
            sz -= 1
        

        