class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        arr = [0 for _ in range(1001)]
        for el in nums1:
            arr[el] += 1
        ans = []
        for el in nums2:
            if arr[el] > 0:
                ans.append(el)
                arr[el] -= 1
        return ans