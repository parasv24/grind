class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        ans = []
        for i in range(numRows):
            for j in range(i, len(s), (numRows * 2) - 2):
                ans.append(s[j])
                if i not in [0, numRows-1]:
                    idx = (numRows - i - 1) * 2
                    if j + idx < len(s):
                        ans.append(s[j+idx])
        return "".join(ans)

        