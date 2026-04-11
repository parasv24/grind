class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # binary search
        # for row in matrix:
        #     l , r = 0 , len(row) - 1
        #     while l <= r:
        #         mid = (l+r) // 2
        #         if row[mid] == target:
        #             return True
        #         if row[mid] < target:
        #             l = mid + 1
        #         else:
        #             r = mid - 1
        # return False

        # O(m+n)

        l, r = 0, len(matrix[0]) - 1
        while l < len(matrix) and r >= 0:
            if matrix[l][r] == target:
                return True
            
            if matrix[l][r] < target:
                l += 1
            else:
                r -= 1
        return False
        
        