class Solution:
    def queensAttacktheKing(self, queens: List[List[int]], king: List[int]) -> List[List[int]]:
        ans = []
        mp = [[0 for _ in range(8)] for _ in range(8)]
        for x,y in queens:
            mp[x][y] = 1
        delta = [[-1, 0], [1, 0], [0, 1], [0, -1], [-1, -1], [1, 1], [-1, 1], [1, -1]]
        for dx, dy in delta:
            kx, ky = king
            while 0 <= kx < 8 and 0 <= ky < 8:
                if mp[kx][ky] == 1:
                    ans.append([kx, ky])
                    break
                kx += dx
                ky += dy 
        return ans