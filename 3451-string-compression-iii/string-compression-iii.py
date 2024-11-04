class Solution:
    def compressedString(self, word: str) -> str:
        ans = ""
        cnt = 1
        for i in range(1, len(word)):
            if word[i] == word[i-1] and cnt < 9:
                cnt += 1
            else:
                ans += f"{cnt}{word[i-1]}"
                cnt = 1
        ans += f"{cnt}{word[-1]}"
        return ans