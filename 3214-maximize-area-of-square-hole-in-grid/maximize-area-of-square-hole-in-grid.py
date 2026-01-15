class Solution:
    def maximizeSquareHoleArea(self, n: int, m: int, hBars: List[int], vBars: List[int]) -> int:
        hBars.sort()
        vBars.sort()
        mx_x = 1
        cur_x = 1
        prev_x = hBars[0]
        for idx in range(1, len(hBars)):
            if hBars[idx] == prev_x + 1:
                cur_x += 1
                mx_x = max(mx_x, cur_x)
            else:
                cur_x = 1
            prev_x = hBars[idx]

        mx_y, cur_y, prev_y = 1, 1, vBars[0]
        for idx in range(1,len(vBars)):
            if vBars[idx] == prev_y+1:
                cur_y += 1
                mx_y = max(mx_y, cur_y)
            else:
                cur_y = 1
            prev_y = vBars[idx]
        # print(mx_x, mx_y)
        side = min(mx_x, mx_y) + 1
        return side * side
        
        
        