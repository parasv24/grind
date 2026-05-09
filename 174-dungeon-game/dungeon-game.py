class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        n , m = len(dungeon), len(dungeon[0])
        @cache
        def is_poss(i, j, health):
            new_health = health + dungeon[i][j]
            if new_health <= 0:
                return False
            if i == n-1 and j == m-1:
                return True
            ans = False
            if i + 1 < n:
                ans = ans or is_poss(i+1, j, new_health)
            if j + 1 < m:
                ans = ans or is_poss(i, j+1, new_health)
            return ans
        l , r = 1, 1000000
        while l <= r:
            mid = (l + r) // 2
            # print(l, r, is_poss(0,0,mid))
            if is_poss(0, 0, mid):
                r = mid - 1
            else:
                l = mid + 1
        return l
        