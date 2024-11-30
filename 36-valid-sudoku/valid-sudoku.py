class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # rows
        for i in range(0,9):
            seen = [ False ] * 10
            for j in range(0,9):
                if board[i][j] != ".":
                    if seen[int(board[i][j])] == True:
                        return False
                    seen[int(board[i][j])] = True
        
        # columns
        for i in range(0,9):
            seen = [ False ] * 10
            for j in range(0,9):
                if board[j][i] != ".":
                    if seen[int(board[j][i])] == True:
                        return False
                    seen[int(board[j][i])] = True

        # checks the box

        idxs = [[0,0], [0,3], [0,6], [3,0], [3,3], [3,6],[6,0],[6,3],[6,6]]
        for x,y in idxs:
            seen = [ False ] * 10
            for i in range(x, x+3):
                for j in range(y,y + 3):
                    if board[i][j] != ".":
                        if seen[int(board[i][j])] == True:
                            return False
                        seen[int(board[i][j])] = True
        return True
        

        