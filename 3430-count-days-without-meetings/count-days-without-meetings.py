class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        meetings.sort(key=lambda x: x[0])
        prev_x , prev_y = meetings[0]
        ans = meetings[0][0] - 1
        print(ans)
        for x,y in meetings:
            if prev_y >= x:
                prev_x = x
                prev_y = max(prev_y, y)
            else:
                print(ans, x, prev_y)
                ans += x - prev_y - 1
                prev_x , prev_y  = x, y
        return ans + days - prev_y


        