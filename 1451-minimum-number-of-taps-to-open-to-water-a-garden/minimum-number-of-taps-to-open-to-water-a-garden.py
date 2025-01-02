class Solution:
    def minTaps(self, n: int, ranges: List[int]) -> int:
        intervals = []
        for i in range(0, len(ranges)):
            if ranges[i]!= 0:
                intervals.append([max(0, i - ranges[i]), min(n,i + ranges[i])])
        intervals.sort(key = lambda x : (x[0], -x[1]))
        if not intervals:
            return -1
        ans = [intervals[0]]
        for itrvl in intervals[1:]:
            if itrvl[1] <= ans[-1][1]:
                pass
            elif itrvl[0] <= ans[-1][1]:
                ans.append(itrvl)
            else:
                if itrvl[0] > ans[-1][1]:
                    return -1
                ans.append(itrvl)
        prev = None
        final_ans = []
        day = 0
        i = 0
        while day <= n and i < len(ans):
            if ans[i][0] <= day <=  ans[i][1]:
                prev = ans[i]
                i += 1
            else:
                if not prev:
                    return -1
                else:
                    final_ans.append(prev)
                    day = prev[1]
                    prev = None
                
        if prev:
            final_ans.append(prev)
        return len(final_ans) if final_ans[-1][1] == n else -1
        