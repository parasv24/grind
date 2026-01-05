class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        rows, cols = len(matrix), len(matrix[0])
        sm = 0
        min_neg = 100000000
        total_neg = 0
        zeroes_count = 0
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] < 0:
                    total_neg += 1
                if matrix[i][j] == 0:
                    zeroes_count += 1
                min_neg = min([abs(matrix[i][j]), min_neg])
                sm += abs(matrix[i][j])
        # print(sm, total_neg, min_neg)
        return sm if (total_neg % 2 == 0 or zeroes_count > 0) else sm - (2 * min_neg)
        