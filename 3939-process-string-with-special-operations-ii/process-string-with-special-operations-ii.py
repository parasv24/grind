class Solution:
    def processStr(self, s: str, k: int) -> str:
        ans = []
        lengths = []
        length = 0
        for ch in s:
            if ch == "*":
                if length > 0:
                    length -= 1
            elif ch == "#":
                length += length
            elif ch == "%":
                length += 0
            else:
                length += 1
            
            lengths.append(length)
            
            if length <= 10 ** 5:
                if ch == "*":
                    if len(ans) > 0:
                        ans.pop()
                elif ch == "#":
                    ans += ans
                elif ch == "%":
                    ans = ans[::-1]
                else:
                    ans.append(ch)
        
        # print(length)
        if length < k + 1:
            return "."
        
        string = "".join(ans)
        i = len(s) - 1
        # print(lengths)
        while i >= 0  and lengths[i] > 10 ** 5:
            if s[i] == "%":
                cur_l = lengths[i]
                k = cur_l - 1 - k
            elif s[i] == "#":
                cur_l = lengths[i]
                k = k % ((cur_l) // 2)
            i -= 1
        return string[k]


        
        