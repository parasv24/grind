class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        vis = [[board[i][j] == "X" for j in range(len(board[0]))] for i in range(len(board))]
        diff = [[0,1], [0,-1], [1, 0], [-1, 0]]
        def dfs(i, j):
            vis[i][j] = True
            for xi ,xj in diff:
                if 0 <=i + xi <len(board) and 0 <= j + xj < len(board[0]) and not vis[i+xi][j+xj]:
                    dfs(i + xi, j + xj)

        for i in range(0, len(board)):
            for j in range(0 , len(board[0])):
                if (i == 0 or i == len(board) - 1 or j == 0 or j == len(board[0]) - 1) and board[i][j] == "O":
                    dfs(i, j)
        
        for i in range(0, len(board)):
            for j in range(0 , len(board[0])):
                if board[i][j] == "O" and not vis[i][j]:
                    board[i][j] = "X"