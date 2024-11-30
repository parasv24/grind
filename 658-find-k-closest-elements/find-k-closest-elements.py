class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        start = 0
        end = len(arr) - 1
        while(end - start + 1 != k):
            if abs(arr[start]-x) <= abs(arr[end]-x):
                end -= 1
            else:
                start += 1
        return arr[start:end+1]
        