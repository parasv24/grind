class Solution:
    def reverseWords(self, s: str) -> str:
        ans = []
        for el in s.split():
            s = list(el)
            s.reverse()
            ans.append("".join(s))
        return " ".join(ans)