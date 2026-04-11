class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        def is_ans(val):
            l, r = 0, len(arr) - 1
            while l <= r:
                mid = (l + r) // 2
                if arr[mid] <= val:
                    l = mid + 1
                else:
                    r = mid - 1
            return val - l
        l , r = 1, 2000
        # ans = -1
        while l <= r:
            mid = (l+r) // 2
            print(l, r, mid, is_ans(mid))
            if is_ans(mid) >= k:
                r = mid - 1
                # ans = mid
            else:
                l = mid + 1
        return l
        