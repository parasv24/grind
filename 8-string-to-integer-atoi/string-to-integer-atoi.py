class Solution:
    def myAtoi(self, s: str) -> int:
        ans = 0
        int_read = False
        sign_read = 1
        valid_values = [chr(i) for i in range(ord('0'), ord('9') + 1)]
        valid_values += [" ", "+", "-"]
        final_ans = 0
        for i in range(len(s)):
            if s[i] not in valid_values:
                final_ans =  ans * sign_read
                break
            else:
                if ord('0') <= ord(s[i]) <= ord('9'):
                    int_read = True
                    ans = ans * 10 + (ord(s[i]) - ord('0'))
                else:
                    if int_read:
                        final_ans = ans * sign_read
                        break
                    if s[i] == "-":
                        sign_read = -1
                    if s[i] in ["+", "-"]:
                        valid_values = [chr(i) for i in range(ord('0'), ord('9') + 1)]
        final_ans = ans * sign_read
        if final_ans < -2147483648:
            return -2147483648
        if final_ans >= 2147483647:
            return 2147483647
        return final_ans
        