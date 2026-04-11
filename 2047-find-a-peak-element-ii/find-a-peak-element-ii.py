class Solution:
    def findPeakGrid(self, mat: List[List[int]]) -> List[int]:
        n , m = len(mat), len(mat[0])
        lo , hi = 0, m -1
        while lo <= hi:
            mid = (lo + hi) // 2
            mx_idx, maxi = -1, -1
            for i in range(n):
                if mat[i][mid] > maxi:
                    mx_idx = i
                    maxi = mat[i][mid]
            print(lo, hi, mid, mx_idx)
            left, right, bottom, top = 0,0,0,0
            if i > 0:
                top = mat[mx_idx-1][mid]
            if i < n-1:
                bottom = mat[mx_idx+1][mid]
            if mid > 0:
                left = mat[mx_idx][mid-1]
            if mid < m-1:
                right = mat[mx_idx][mid+1]
            
            if  left < mat[mx_idx][mid] > right and top < mat[mx_idx][mid] > bottom:
                return [mx_idx, mid]
            
            if left > mat[mx_idx][mid]:
                hi = mid - 1
            else:
                lo = mid + 1
        return [-1, -1]

        