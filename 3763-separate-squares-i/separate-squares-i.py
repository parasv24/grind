class Solution:
    def separateSquares(self, squares: List[List[int]]) -> float:
        def area(cut):
            ans = 0
            for el in squares:
                x, y, l = el
                if y > cut:
                    continue
                if y + l > cut:
                    ans += (cut - y) * (l)
                else:
                    ans += l * l
            return ans * 1.0

        start = 0
        end = 2000000000
        total = area(end + 10)
        target = round(total / 2, 5)
        while (end - start) > 1e-5:
            mid = (start + end) / 2
            val = area(mid)
            # print(start, end, mid, val, target)
            if val < target:
                start = mid
            else:
                end = mid
        return start



            
        