class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        arr.sort()
        prev = 1
        for el in arr[1:]:
            if el == prev:
                continue
            else:
                prev = prev + 1
        return prev


        