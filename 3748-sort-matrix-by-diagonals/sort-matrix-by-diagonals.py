class Solution:
    def sortMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        mp = {}
        n = len(grid)
        
        for i in range(n):
            for j in range(n):
                if (i-j) not in mp:
                    mp[i-j] = [[], 0]
                mp[i-j][0].append(grid[i][j])
        
        for key in mp.keys():
            if key < 0:
                mp[key][0].sort()
            else:
                mp[key][0].sort(reverse=True)
        
        for i in range(n):
            for j in range(n):
                grid[i][j] = mp[i-j][0][mp[i-j][1]]
                mp[i-j][1] += 1

        return grid


