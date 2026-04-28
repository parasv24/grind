class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        sorted_list = sorted([el for row in grid for el in row])
        ans = 0
        median = sorted_list[len(sorted_list) // 2]
        for num in sorted_list:
            if num % x != median % x:
                return -1
            ans += abs(median - num) // x
        return ans


        