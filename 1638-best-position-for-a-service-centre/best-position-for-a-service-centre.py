class Solution:
    def getMinDistSum(self, positions: List[List[int]]) -> float:
        # Distance function
        def f(x, y):
            return sum(math.hypot(x - px, y - py) for px, py in positions)
        
        # Start from centroid (good initial guess)
        x = sum(px for px, _ in positions) / len(positions)
        y = sum(py for _, py in positions) / len(positions)
        
        # Initial step size
        step = 100.0
        
        # Directions: right, left, up, down
        dirs = [(1,0), (-1,0), (0,1), (0,-1)]
        
        best = f(x, y)
        
        while step > 1e-6:
            improved = False
            
            for dx, dy in dirs:
                nx, ny = x + dx * step, y + dy * step
                val = f(nx, ny)
                
                if val < best:
                    x, y = nx, ny
                    best = val
                    improved = True
                    break  # move immediately
            
            # If no direction improved → shrink step
            if not improved:
                step /= 2
        
        return best

        