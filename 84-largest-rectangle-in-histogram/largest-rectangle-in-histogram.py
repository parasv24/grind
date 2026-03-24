class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stck = []
        nxt_small = [-1 for _ in range(len(heights))]
        for i in range(len(heights) - 1, -1, -1):
            if len(stck) > 0:
                while len(stck) > 0 and heights[stck[-1]] >= heights[i]:
                    stck.pop()
                nxt_small[i] = stck[-1] if len(stck) > 0 else -1
            stck.append(i)
        prev_small = [-1 for _ in range(len(heights))]
        stck = []
        for i in range(len(heights)):
            while len(stck) > 0 and heights[stck[-1]] >= heights[i]:
                stck.pop()
            prev_small[i] = stck[-1] if len(stck) > 0 else -1 
            stck.append(i)
        ans = -1
        for i in range(len(heights)):
            prev_max = heights[i] * (i - prev_small[i]) if prev_small[i] == -1 else heights[i] * (i - prev_small[i])
            next_max = heights[i] * (len(heights) - i) if nxt_small[i] == -1 else heights[i] * (nxt_small[i] - i)
            prev_max += (next_max - heights[i])
            cur = heights[i]
            ans = max(ans, cur, next_max, prev_max)
        return ans


        