class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        maxi = 0
        for m in range(ord('A'), ord('Z') + 1):
            i , j, used = 0, 0, 0
            char = chr(m)
            while j < len(s):
                if s[j] == char or used < k:
                    if s[j] != char:
                        used += 1
                    j += 1
                elif k > 0:
                    while i < j and used >= k:
                        if s[i] != char:
                            used -= 1
                        i += 1
                else:
                    i = j + 1
                    j += 1
                maxi = max(maxi, j - i)
        return maxi
            
        