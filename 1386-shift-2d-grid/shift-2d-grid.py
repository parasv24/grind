from typing import List

class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        n = len(grid)
        m = len(grid[0])

        temp = []

        # Flatten the grid
        for i in range(n):
            for j in range(m):
                temp.append(grid[i][j])

        size = len(temp)
        k %= size

        # Reverse helper
        def reverse(arr, left, right):
            while left < right:
                arr[left], arr[right] = arr[right], arr[left]
                left += 1
                right -= 1

        # Rotate using reversal algorithm
        reverse(temp, 0, size - 1)
        reverse(temp, 0, k - 1)
        reverse(temp, k, size - 1)

        # Reconstruct the grid
        result = []
        idx = 0
        for i in range(n):
            row = []
            for j in range(m):
                row.append(temp[idx])
                idx += 1
            result.append(row)

        return result