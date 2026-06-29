class Solution:
    def numOfStrings(self, patterns: List[str], word: str) -> int:
        ans = 0
        for pat in patterns:
            if pat in word:
                ans += 1
        return ans
        