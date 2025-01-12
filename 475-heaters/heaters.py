class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        houses.sort()
        lo , hi = 0, max(houses[-1],max(heaters))
        def can_sweep(num):
            line = {}
            for i in houses:
                line[i] = line.get(i, 0) + 0
            for j in heaters:
                left = max(0, j - num)
                right = min(houses[-1]+ 1, j + num + 1)
                line[left] = line.get(left, 0) - 1
                line[right] = line.get(right, 0) + 1
            prev = 0
            for i in sorted(line.keys()):
                prev += line[i]
                line[i] = prev
            for i in houses:
                if line[i]>=0:
                    return False
            return True
        ans = -1
        while lo <= hi:
            mid = (lo + hi) // 2
            if can_sweep(mid):
                hi = mid -1
                ans = mid
            else:
                lo = mid + 1
        return ans
        