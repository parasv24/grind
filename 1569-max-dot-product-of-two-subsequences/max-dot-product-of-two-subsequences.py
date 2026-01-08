class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        m = len(nums2)
        @cache
        def rec(i,j):
            if i >= n or j >= m:
                return -100000000
            
            ans1 = rec(i+1, j+1)
            if ans1 < 0:
                ans1 = 0
            ans1 += nums1[i]*nums2[j]
            ans2 = rec(i+1, j)
            ans3 = rec(i , j+1)
            return max([ans1, ans2, ans3])
        return rec(0,0)
