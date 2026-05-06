class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:
        # 4 ^ n solution = 4 ^ 30 = 1 e 18
        # def rec(i, j):
        #     if i == j:
        #         return set(s1[i])
        #     ans = set()
        #     for k in range(i, j):
        #         left_ans = rec(i, k)
        #         right_ans = rec(k+1, j)
        #         for x in left_ans:
        #             for y in right_ans:
        #                 ans.add(x+y)
        #                 ans.add(y+x)
        #     return ans
        # ans = rec(0, len(s1) - 1)
        # return s2 in ans
        @cache
        def rec(i, j , length):
            if s1[i: i+ length] == s2[j: j+length]:
                return True
            
            for k in range(1, length):
                if rec(i, j, k) and rec(i+k, j+k, length - k):
                    return True
                
                if rec(i, j + length - k , k) and rec(i+k, j, length - k):
                    return True
            return False
        return rec(0,0, len(s1))

        