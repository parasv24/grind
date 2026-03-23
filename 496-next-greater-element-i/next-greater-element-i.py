class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stck = []
        ng_arr = {el: -1 for el in nums2}
        for i in range(len(nums2) - 1, -1, -1):
            if len(stck) > 0:
                while len(stck) > 0 and stck[-1] < nums2[i]:
                    stck.pop()
                ng_arr[nums2[i]] = stck[-1] if len(stck) > 0 else -1
            stck.append(nums2[i])
        return [ng_arr[el] for el in nums1]
        