class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        other_color = -1
        ans = -1
        for i in range(0, len(colors)):
            if colors[i] == colors[0] and other_color != -1:
                ans = max(ans, i - other_color)
            elif colors[i] != colors[0]:
                if other_color == -1:
                    other_color = i
                ans = max(ans, i)
        return ans
        