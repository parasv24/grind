class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        line = [0] * (len(s)+1)
        for x, y, z in shifts:
            if z == 0:
                line[x] -= 1
                line[y+1] += 1
            else:
                line[x] += 1
                line[y + 1] -= 1
        for i in range(1, len(s)):
            line[i] += line[i - 1]
        #print(line)
        ans = []
        for i in range(0, len(s)):
            shift = (abs(line[i]) % 26)
            if line[i] < 0:
                shift *= -1
            #print(shift, abs(line[i]) % 26, )
            val = ord(s[i]) + shift
            if val < 97:
                val += 26
            if val >= 97 + 26:
                val -= 26
            ans.append(chr(val))
        return "".join(ans)            

        