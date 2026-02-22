class Solution:
    def binaryGap(self, n: int) -> int:
        rep = ""
        while n > 0:
            n , mod = divmod(n, 2)
            rep += str(mod)
        maxi = 0
        prev = -1
        for i in range(0, len(rep)):
            if rep[i] == '1':
                if prev >= 0:
                    maxi = max(maxi, i - prev)
                prev = i
        return maxi
        