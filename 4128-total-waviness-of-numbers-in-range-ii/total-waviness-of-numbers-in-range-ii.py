class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:
        def get_count(num):
            s = str(num)
            @cache
            def rec(i, limit_on, prev2, prev1):
                if i == len(s):
                    return (1, 0)
                
                limit = int(s[i]) if limit_on else 9
                ways, total = 0, 0
                for j in range(0, limit + 1):
                    new_limit_on = limit_on and j == limit
                    if j == 0 and prev2 == -1:
                        x, y = rec(i+1, new_limit_on, -1, -1)
                        total += x
                        ways += y
                        continue
                    
                    if prev2 == -1:
                        next_prev2 = j
                        next_prev1 = -1
                    elif prev1 == -1:
                        next_prev2 = prev2
                        next_prev1 = j
                    else:
                        next_prev2 = prev1
                        next_prev1 = j
                    x, y = rec(i+1, new_limit_on, next_prev2, next_prev1)
                    if prev2 != -1 and prev1 != -1:
                        ways += (1 * x) if (prev2 < prev1 > j) or (prev2 > prev1 < j) else 0
                    total += x
                    ways += y
                return (total, ways)
            return rec(0, True, -1, -1)[1]
        return get_count(num2) - get_count(num1-1)




        

