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

        if length < k + 1:
            return "."
        
        i = len(s) - 1
        while i >= 0 and lengths[i] >= 0:
            if lengths[i] == k + 1 and s[i] not in ["#", "%", "*"]:
                return s[i]
            if s[i] == "%":
                cur_l = lengths[i]
                k = cur_l - 1 - k
            elif s[i] == "#":
                cur_l = lengths[i]
                k = k % ((cur_l) // 2)
            i -= 1
        return "."


        
        