class Solution:
    def kthSmallest(self, mat: List[List[int]], k: int) -> int:
        # brute force
        n, m = len(mat), len(mat[0])
        def rec(i):
            if i == n:
                return [0]
            ans = []
            small_ans = rec(i+1)
            # print(small_ans)
            for j in range(m):
                for el in small_ans:
                    if len(ans) < k:
                        heappush(ans, (el + -mat[i][j]))
                    else:
                        if (-el + mat[i][j]) < -ans[0]:
                            heapreplace(ans, (el - mat[i][j]))
            return ans
        ans = rec(0)
        return -ans[0]




        

