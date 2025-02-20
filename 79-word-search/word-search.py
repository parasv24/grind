class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        n, m = len(board), len(board[0])
        def is_possible(i, j, idx):
            if idx == len(word):  # Base case: If all characters are matched
                return True

            if i < 0 or i >= n or j < 0 or j >= m or board[i][j] != word[idx]:  # Out of bounds or mismatch
                return False

            # Mark as visited by modifying board temporarily
            temp, board[i][j] = board[i][j], '#'

            # Explore all 4 directions
            found = (is_possible(i + 1, j, idx + 1) or
                    is_possible(i - 1, j, idx + 1) or
                    is_possible(i, j + 1, idx + 1) or
                    is_possible(i, j - 1, idx + 1))

            # Restore original character (backtracking)
            board[i][j] = temp

            return found

        for i in range(n):
            for j in range(m):
                if board[i][j] == word[0] and is_possible(i, j, 0):
                    return True

        return False

        