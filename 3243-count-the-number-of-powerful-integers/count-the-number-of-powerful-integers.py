class Solution:
    def numberOfPowerfulInt(self, start: int, finish: int, limit: int, s: str) -> int:
        def get_count(string):
            string = str(string)
            if len(string) < len(s):
                return 0
            if len(string) == len(s) and s > string:
                return 0
            for ch in s:
                if int(ch) > limit:
                    return 0
            @cache
            def rec(i, limit_on):
                if i == len(string):
                    return 1
                if i >= (len(string) - len(s)):
                    if not limit_on:
                        return 1
                    j = i - len(string) + len(s)
                    if string[i] > s[j]:
                        return 1
                    if string[i] < s[j]:
                        return 0
                    return rec(i+1, True)
                
                restriction = min(limit, int(string[i])) if limit_on else min(limit, 9)

                ans = 0
                for j in range(0, restriction + 1):
                    ans += rec(i+1, limit_on and j == int(string[i]))
                return ans
            return rec(0, True)
        return get_count(finish) - get_count(start - 1)
                    
