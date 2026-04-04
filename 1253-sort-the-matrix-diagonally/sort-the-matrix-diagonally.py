class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        diagonals = defaultdict(list)
        n , m = len(mat), len(mat[0])
        for i in range(n):
            for j in range(m):
                diagonals[i-j].append(mat[i][j])
        # print(diagonals)
        for key, values in diagonals.items():
            values.sort(reverse=True)
        
        for i in range(n):
            for j in range(m):
                val = diagonals[i-j].pop()
                mat[i][j] = val
        # print(diagonals)
        return mat
        