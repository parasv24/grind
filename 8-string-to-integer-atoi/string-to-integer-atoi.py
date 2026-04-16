class Solution:
    def myAtoi(self, s: str) -> int:
        i = 0
        pos = 1
        while i < len(s) and s[i] == " ":
            i += 1
        if i < len(s) and s[i] == "-":
            pos = -1
            i += 1
        elif i < len(s) and s[i] == "+":
            i += 1
        ans = 0
        while i < len(s) and "0" <= s[i] <= "9":
            ans = ans * 10 + (ord(s[i]) - 48)
            i += 1
        ans = ans * pos

        if ans  < -2147483648:
            return -2147483648
        if ans > 2147483647:
            return 2147483647
        return ans
