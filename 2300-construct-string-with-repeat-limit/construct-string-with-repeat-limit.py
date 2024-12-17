class Solution:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        a = [0] * 26
        for i in s:
            a[ord(i) - 97] += 1
        ans = ""
        limit = 0
        i = 25
        while i > -1:
            # print(i," ", ans)
            if a[i] > repeatLimit:
                a[i] -= repeatLimit
                limit = repeatLimit
                ans += repeatLimit * chr(97 + i)
                j = i - 1
                while j > -1:
                    if a[j] > 0:
                        ans += chr(97+j)
                        a[j] -= 1
                        limit = 0
                        break
                    j -= 1
                if limit == repeatLimit:
                    break
            else:
                ans += a[i] * chr(97 + i)
                a[i] -= repeatLimit
                i -= 1
        # print(ans)
        return ans

        
        