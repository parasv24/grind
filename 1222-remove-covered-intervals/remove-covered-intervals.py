class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: (x[0], -x[1]))
        ans = [intervals[0]]
        for itrvl in intervals[1:]:
            if ans[-1][0] <= itrvl[0]  and itrvl[1] <= ans[-1][1]:
                pass
            else:
                ans.append(itrvl)
        return len(ans)
        