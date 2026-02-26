class Solution:
    def numSteps(self, s: str) -> int:
        def addone(s):
            for i in range(len(s) - 1, -1, -1):
                if s[i] == "0":
                    return s[:i] + "1" + s[i+1: len(s) - 1]
            return "1" + (len(s) - 1) * "0"            
        ans  = 0
        while s != "1":
            # print(s, ans)
            if s[-1] == "1":
                s = addone(s)
                ans += 2
            else:
                s = s[:len(s) - 1]
                ans += 1
        return ans

        