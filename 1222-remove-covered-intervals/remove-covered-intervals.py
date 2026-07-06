class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key= lambda x: (x[0], -x[1]))
        prev0, prev1 = intervals[0]
        count = 1
        for x, y in intervals[1:]:
            if prev0 <= x and y <= prev1:
                continue
            else:
                prev0, prev1 = x, y
                count += 1
        return count
        