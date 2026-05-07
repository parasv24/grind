class Solution:
    def numSplits(self, s: str) -> int:
        left_uniqs = [0] * len(s)
        right_uniqs = [0] * len(s)
        st = set()
        rst = set()
        for i in range(len(s)):
            st.add(s[i])
            left_uniqs[i] = len(st)
            right_uniqs[len(s) - 1- i] = len(rst)
            rst.add(s[len(s) - 1- i])
        ans = 0
        for i in range(len(s)-1):
            if left_uniqs[i] == right_uniqs[i]:
                ans += 1
        return ans

        