class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:
        def get_count(s):
            s = str(s)
            @cache
            def p_and_v(i, limit_on, prev2, prev1, started):
                if i == len(s):
                    return (1, 0)
                
                limit = int(s[i]) if limit_on else 9
                total_w = 0
                ans = 0
                for j in range(0, limit + 1):
                    new_started = started or j != 0
                    if not new_started:
                        total, small_ans = p_and_v(i+1, limit_on and j == limit, -1, -1, False)
                        ans += small_ans
                        total_w += total
                    else:
                        peak = 0
                        valley = 0

                        # Only check after we have 3 digits
                        if prev2 != -1 and prev1 != -1:
                            peak = 1 if prev2 < prev1 > j else 0
                            valley = 1 if prev2 > prev1 < j else 0
                        cur = peak + valley
                        total, small_ans = p_and_v(i+1, limit_on and j == limit, prev1, j, True)
                        ans += small_ans + (cur * total)
                        total_w += total
                return (total_w, ans)
            return p_and_v(0, True, -1, -1, False)[1]
        return get_count(num2) - get_count(num1-1)
        

