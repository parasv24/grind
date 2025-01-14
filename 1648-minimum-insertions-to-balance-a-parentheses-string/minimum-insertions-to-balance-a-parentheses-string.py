class Solution:
    def minInsertions(self, s: str) -> int:
        s += "."
        stck = []
        ans = 0
        i = 0
        while i < (len(s)-1):
            if s[i] == "(":
                stck.append(s[i])
            else:
                if len(stck) == 0:
                    if s[i+1] == ")":
                        ans += 1
                        i += 1
                    else:
                        ans += 2
                else:
                    stck.pop()
                    if s[i+1] == ")":
                        ans += 0
                        i += 1
                    else:
                        ans += 1
            i+=1        
        ans += len(stck) * 2
        return ans

        