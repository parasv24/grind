class Solution:
    def maxScore(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])

        ans = float('-inf')

        def kadane_len_at_least_2(arr):
            best = float('-inf')

            # start with length 2
            curr = arr[0] + arr[1]
            best = curr

            for i in range(2, len(arr)):
                curr = max(curr + arr[i], arr[i - 1] + arr[i])
                best = max(best, curr)

            return best

        # Row overlaps
        for i in range(n):
            ans = max(ans, kadane_len_at_least_2(grid[i]))

        # Column overlaps
        for j in range(m):
            col = [grid[i][j] for i in range(n)]
            ans = max(ans, kadane_len_at_least_2(col))

        # Single-cell overlap (must be interior)
        for i in range(1, n - 1):
            for j in range(1, m - 1):
                ans = max(ans, grid[i][j])

        return ans