class Solution:
    def makeFancyString(self, s: str) -> str:
        cnt = 0
        ans = 0
        prev = "-1"
        output = ""
        for el in s:
            if el == prev:
                cnt += 1
                if cnt >= 2:
                    ans += 1
                    continue
                output += el    
            else:
                cnt = 0
                output += el
            prev = el
        return output
        