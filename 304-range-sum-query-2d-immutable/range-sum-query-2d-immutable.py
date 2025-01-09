class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        n = len(matrix)
        m = len(matrix[0])
        self.p_sum = [[0] * m for _ in range(n)]
        for i in range(0, n):
            for j in range(0, m):
                val = 0
                if i > 0:
                    val += self.p_sum[i-1][j]
                if j > 0:
                    val += self.p_sum[i][j-1]
                if i > 0 and j > 0:
                    val -= self.p_sum[i-1][j-1]
                self.p_sum[i][j] = val + matrix[i][j]
        
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        val = 0
        if col1-1 >=0:
            val -= self.p_sum[row2][col1-1]
        if row1 - 1 >= 0:
            val -= self.p_sum[row1-1][col2]
        if row1 - 1 >=0 and col1-1 >=0:
            val += self.p_sum[row1-1][col1-1]
        return self.p_sum[row2][col2] + val
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)