class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ans = strs[0]
        for el in strs[1:]:
            i = 0
            while i < len(ans) and i < len(el):
                if ans[i] == el[i]:
                    i += 1
                else:
                    break
            if i == 0:
                return ""
            else:
                ans = ans[0: i]
        return ans
        