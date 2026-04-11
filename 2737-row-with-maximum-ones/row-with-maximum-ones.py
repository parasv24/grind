class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
        for row in mat:
            row.sort()
        ans = [-1, -1]
        for idx, row in enumerate(mat):
            l, r =0, len(row) - 1
            while l <= r:
                mid = (l + r) // 2
                if row[mid] >= 1:
                    r = mid - 1
                else:
                    l = mid + 1
            left = l
            l, r = 0, len(row) - 1
            while l <= r:
                mid = (l+r) // 2
                if row[mid] <= 1:
                    l = mid + 1
                else:
                    r = mid - 1
            if l - left > ans[1]:
                ans = [idx, l-left]
        return ans
        