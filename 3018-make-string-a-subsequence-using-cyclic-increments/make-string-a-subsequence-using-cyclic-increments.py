class Solution:
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        def get_prev(ch):
            if ch == "z":
                return "a"
            else:
                return chr(ord(ch) + 1)
        i = j = 0
        while(i < len(str1) and j < len(str2)):
            if str1[i] == str2[j] or get_prev(str1[i]) == str2[j]:
                i += 1
                j +=1
            else:
                i += 1
        if j == len(str2):
            return  True
        return False

