class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        pattern = []
        for i in range(len(p)):
            if p[i] == "*":
                if i > 0 and p[i-1] != "*":
                    pattern[-1] += ord(p[i])
            else:
                pattern.append(ord(p[i]))
        # print(pattern)
        @cache
        def rec(i, j):
            # print(i,j)
            if i == len(s) and j == len(pattern):
                return True
            if i == len(s):
                if pattern[j] == 88 or pattern[j] > 122:
                    return rec(i, j+1)
                else:
                    return False

            if i == len(s) or j == len(pattern):
                return False
            
            if  97 <= pattern[j] <= 122:
                if s[i] != chr(pattern[j]):
                    return False
                return rec(i+1, j+1)
            elif pattern[j] == 46:
                return rec(i+1, j+1)
            else:
                char = chr(pattern[j] - 42)
                if s[i] == char or char == ".":
                    return rec(i+1, j+1) or rec(i+1, j) or rec(i, j+1)
                else:
                    return rec(i, j+1)
        return rec(0, 0)


        
        

        