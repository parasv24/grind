class Solution:
    def numberOfBeautifulIntegers(self, low: int, high: int, k: int) -> int:
        def get_count(num):
            s = str(num)
            @cache
            def rec(i, limit_on, started, cnt, rem):
                if i == len(s):
                    return (cnt == 0) and (rem == 0) and started
                limit = int(s[i]) if limit_on else 9
                
                ans = 0
                for j in range(0, limit + 1):
                    l_on = limit_on and j == limit
                    if not started and j == 0:
                        ans += rec(i+1, l_on, False, 0, 0)
                        continue
                    cnt_val = 1 if (j % 2 == 0) else -1
                    new_rem = (rem * 10 + j) % k
                    ans += rec(i+1, l_on, True, cnt + cnt_val, new_rem)
                return ans
            return rec(0, True, False, 0, 0)
        return get_count(high) - get_count(low - 1)


                