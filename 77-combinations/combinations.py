class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []
        def rec(i, arr):
            if i > n:
                return
            rec(i+1, arr)
            if len(arr) == k - 1:
                ans.append(arr + [i])
                return
            rec(i+1, arr + [i])
        rec(1, [])
        return ans