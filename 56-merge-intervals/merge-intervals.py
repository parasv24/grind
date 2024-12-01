class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        res = []
        prev = intervals[0]
        i = 1
        while i < len(intervals):
            # print(i, prev)
            if prev[1] >= intervals[i][0]:
                prev[1] = max(prev[1], intervals[i][1])
            else:
                res.append(prev)
                prev = intervals[i]
            i += 1
        res.append(prev)
        return res
        