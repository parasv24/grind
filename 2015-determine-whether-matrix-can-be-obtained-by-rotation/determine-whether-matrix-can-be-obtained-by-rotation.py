class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        n = len(mat)
        def check_same(n):
            for i in range(n):
                for j in range(n):
                    if mat[i][j] != target[i][j]:
                        return False
            return True

        iters = 4
        while iters > 0:
            if check_same(n):
                return True
            for i in range(n // 2):
                for j in range(i, n - i - 1):
                    temp = mat[i][j]

                    mat[i][j] = mat[n - 1 - j][i]
                    mat[n - 1 - j][i] = mat[n - 1 - i][n - 1 - j]
                    mat[n - 1 - i][n - 1 - j] = mat[j][n - 1 - i]
                    mat[j][n - 1 - i] = temp

            iters -= 1
        return False
                
        