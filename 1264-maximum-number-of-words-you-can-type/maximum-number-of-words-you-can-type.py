class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        broken = [0] * 26
        for i in brokenLetters:
            broken[ord(i) - 97] = 1
        ans = 0
        for word in text.split(" "):
            flag = False
            for ch in word:
                if broken[ord(ch) - 97] == 1:
                    flag = True
                    break
            if flag == False:
                ans += 1
        return ans