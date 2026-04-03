class Solution:
    def maxWalls(self, robots: List[int], distance: List[int], walls: List[int]) -> int:
        n = len(robots)
        
        robots_data = sorted(zip(robots, distance))
        walls.sort()
        
        left = [0] * n
        right = [0] * n
        between = [0] * n   # walls between i-1 and i
        
        for i in range(n):
            pos, dist = robots_data[i]
            
            # ---------- LEFT ----------
            left_limit = pos - dist
            if i > 0:
                left_limit = max(left_limit, robots_data[i-1][0] + 1)
            
            l = bisect_left(walls, left_limit)
            r = bisect_right(walls, pos)
            left[i] = r - l
            
            # ---------- RIGHT ----------
            right_limit = pos + dist
            if i < n - 1:
                right_limit = min(right_limit, robots_data[i+1][0] - 1)
            
            l = bisect_left(walls, pos)
            r = bisect_right(walls, right_limit)
            right[i] = r - l
            
            # ---------- BETWEEN ----------
            if i > 0:
                l = bisect_left(walls, robots_data[i-1][0])
                r = bisect_right(walls, pos)
                between[i] = r - l
        
        # ---------- DP ----------
        prev_left = left[0]
        prev_right = right[0]
        
        for i in range(1, n):
            
            # LEFT choice
            current_left = max(
                prev_left + left[i],  # LL
                
                # RL with overlap handling
                prev_right - right[i-1] + min(left[i] + right[i-1], between[i])
            )
            
            # RIGHT choice
            current_right = max(
                prev_left + right[i],   # LR
                prev_right + right[i]   # RR
            )
            
            prev_left, prev_right = current_left, current_right
        
        return max(prev_left, prev_right)
        