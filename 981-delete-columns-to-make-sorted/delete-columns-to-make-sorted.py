class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        valid_columns = [0] * len(strs[0])
        prev = strs[0]
        for string in strs[1:]:
            for idx, ch in enumerate(string):
                if valid_columns[idx] == 0:
                    if string[idx] < prev[idx]:
                        valid_columns[idx] = 1
            prev = string                 
        return sum(valid_columns)
        