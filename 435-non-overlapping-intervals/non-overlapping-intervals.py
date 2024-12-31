class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[1])
        ans = 1
        prev = intervals[0][1]
        for x, y in intervals[1:]:
            if x >= prev:
                prev = y
                ans += 1
        return len(intervals) - ans
        