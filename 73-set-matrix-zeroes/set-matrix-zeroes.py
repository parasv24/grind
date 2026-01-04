class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        row = len(matrix)
        col = len(matrix[0])
        arr = []
        for i in range(row):
            for j in range(col):
                if matrix[i][j] == 0:
                    if i!= 0 and j!=0:
                        matrix[i][0] = 0
                        matrix[0][j] = 0
                    if i == 0:
                        arr.append("row")
                    if j == 0:
                        arr.append("col")
        for i in range(1, row):
            for j in range(1, col):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
        if "row" in arr:
            for j in range(col):
                matrix[0][j] = 0
        if "col" in arr:
            for j in range(row):
                matrix[j][0] = 0

        
        

