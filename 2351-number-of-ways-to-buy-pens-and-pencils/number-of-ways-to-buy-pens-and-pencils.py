class Solution:
    def waysToBuyPensPencils(self, total: int, cost1: int, cost2: int) -> int:
        init = 0
        ans = 0
        while True:
            ans += ((total - init) // cost2) + 1
            # print(init, ans)
            init += cost1
            if init > total:
                break
        return ans

        