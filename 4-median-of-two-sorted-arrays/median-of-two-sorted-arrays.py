class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        leng = len(nums1) + len(nums2)
        def get_ele(arrays, k):
            low, high = -1000000, 1000000
            final_ans = -1
            while low <= high:
                target = (low + high) // 2
                ans  = 0
                for arr in arrays:
                    start, end = 0, len(arr) - 1
                    while start <= end:
                        mid = (start + end) // 2
                        if arr[mid] <= target:
                            start = mid + 1
                        else:
                            end = mid - 1
                    ans += start
                if ans <= k - 1:
                    low = target + 1
                else:
                    final_ans = target
                    high = target - 1
            return final_ans

        if leng % 2 == 0:
            return (get_ele([nums1, nums2], leng // 2 + 1) + get_ele([nums1, nums2], (leng) // 2)) / 2
        else:
            return get_ele([nums1, nums2], leng // 2 + 1)
        