class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        min_x = 100000000
        ans = []
        for i in range(1, len(arr)):
            min_x = min(min_x, abs(arr[i] - arr[i-1]))
        for i in range(1, len(arr)):
            if abs(arr[i] - arr[i-1]) == min_x:
                ans.append([arr[i-1], arr[i]])
        return ans
        