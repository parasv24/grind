class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        unfilled = []
        n = 9
        cols = [set() for i in range(9)]
        rows = [set() for i in range(9)]
        quads = [set() for i in range(9)]
        for i in range(n):
            for j in range(n):
                if board[i][j] == ".":
                    unfilled.append((i,j))
                else:
                    val = int(board[i][j])
                    cols[j].add(val)
                    rows[i].add(val)
                    quad = (i // 3) * 3 + (j // 3)
                    quads[quad].add(val)
        
        def rec(i):
            if i == len(unfilled):
                return True
            di, dj = unfilled[i]
            # print(i, di, dj, cols[dj], rows[di])
            for k in range(1, 10):
                quad = (di // 3) * 3 + (dj // 3)
                if k not in cols[dj] and k not in rows[di] and k not in quads[quad]:
                    # print(di, dj, k)
                    board[di][dj] = str(k)
                    cols[dj].add(k)
                    rows[di].add(k)
                    quads[quad].add(k)
                    next_ans = rec(i+1)
                    if next_ans:
                        return True
                    board[di][dj] = "."
                    cols[dj].remove(k)
                    rows[di].remove(k)
                    quads[quad].remove(k)
            return False
        rec(0)

                    

        