class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        arr = [0]*101
        for i, j in logs:
            arr[i - 1950] += 1
            if j < 2050:
                arr[j - 1950] -= 1
        mx = max(arr[0], 0)
        ans = 0
        for i in range(1,101):
            arr[i] += arr[i-1]
            if arr[i] > mx:
                mx = max(arr[i], mx)
                ans = i
        return 1950 + ans

        
        