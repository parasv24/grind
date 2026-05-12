class Solution:
    def minimumEffort(self, tasks: List[List[int]]) -> int:
        tasks.sort(key= lambda x: (-(x[1]-x[0]), -x[0]))

        def is_poss(val):
            for actual, minimum in tasks:
                if minimum > val:
                    return False
                val -= actual
            return val >= 0

        l, r = 0, 10 ** 9
        while l <= r:
            mid = (l + r) // 2
            if is_poss(mid):
                r = mid - 1
            else:
                l = mid + 1
        return l
        