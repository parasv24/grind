class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        i, j = 0, 0
        while n > 1:
            ci, cj = i, j
            print(ci, cj)
            for beta in range(n-1):
                matrix[ci][cj+beta], matrix[ci+beta][cj+n-1],matrix[ci+n-1][cj+n-1-beta],matrix[ci+n-1-beta][cj]=matrix[ci+n-1-beta][cj], matrix[ci][cj+beta],matrix[ci+beta][cj+n-1],matrix[ci+n-1][cj+n-1-beta]
            n -= 2
            i +=1
            j += 1
        
        