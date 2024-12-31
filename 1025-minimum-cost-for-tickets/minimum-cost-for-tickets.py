class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        @cache
        def helper(i):
            if i >= len(days):
                return 0
            day_1 = costs[0] + helper(i+1)
            val = days[i] + 6
            j  = i + 1
            while j < len(days):
                if days[j] <= val:
                    j += 1
                else:
                    break
            day_7 = costs[1] + helper(j)
            val = days[i] + 29
            j  = i + 1
            while j < len(days):
                if days[j] <= val:
                    j += 1
                else:
                    break
            day_30 = costs[2] + helper(j)
            return min(day_1, day_7, day_30)
        return helper(0)

                

        