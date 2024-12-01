class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ans = strs[0]
        for i in range(1, len(strs)):
            new_ans = ""
            for j in range(0, min(len(strs[i]), len(ans))):
                if strs[i][j] == ans[j]:
                    new_ans += strs[i][j]
                else:
                    break
            ans = new_ans
            if ans == "":
                return ans
        return ans
            
        