class Solution:
    def addMinimum(self, word: str) -> int:
        str1 = "abc"
        ans = 0
        j = 0
        i = 0
        while i < len(word):
            if  j > 2:
                j = 0
            if word[i] == str1[j]:
                i += 1
                j += 1
            else:
                ans += 1
                j += 1
        if word[-1] == "b":
            ans += 1
        if word[-1] == "a":
            ans += 2
        return ans


                
        