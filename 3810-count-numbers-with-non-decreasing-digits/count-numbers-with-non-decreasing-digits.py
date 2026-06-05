class Solution:
    def countNumbers(self, l: str, r: str, b: int) -> int:
        MOD = 10 ** 9 + 7
        def convert_base(num_str, new_base):
            if num_str == "0":
                return "0"

            result = []

            while num_str != "0":
                quotient = []
                remainder = 0

                for ch in num_str:
                    curr = remainder * 10 + int(ch)
                    quotient_digit = curr // new_base
                    remainder = curr % new_base

                    # Avoid leading zeros
                    if quotient or quotient_digit != 0:
                        quotient.append(str(quotient_digit))

                result.append(str(remainder))
                num_str = ''.join(quotient) if quotient else "0"

            return ''.join(reversed(result))

        def get_count(s):
            @cache
            def rec(i, limit_on, started, prev):
                if i == len(s):
                    return 1
                limit = int(s[i]) if limit_on else b-1

                ans = 0
                for j in range(prev, limit + 1):
                    new_l_on = limit_on and j == limit
                    if not started and j == 0:
                        ans += rec(i+1, new_l_on, False, 0)
                        continue
                    ans += rec(i+1, new_l_on, True, j)
                return ans
            return rec(0, True, False, 0) % MOD
        l , r = convert_base(l, b), convert_base(r, b)
        valid = True
        prev = int(l[0])
        for ch in l[1:]:
            if int(ch) >= prev:
                prev = int(ch)
            else:
                valid = False
                break
        
        return (get_count(r) - get_count(l) + valid)% MOD


        