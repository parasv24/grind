class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x: x[1])
        ans = 1
        prev = points[0][1]
        for x, y in points[1:]:
            if x > prev:
                prev = y
                ans += 1
        return ans


        