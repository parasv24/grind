class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        l, r = max(nums), sum(nums)
        def is_poss(min_sum):
            cur = 0
            total_sub = 0
            for el in nums:
                if cur + el <= min_sum:
                    cur += el
                else:
                    cur = el
                    total_sub += 1
            if cur > 0:
                total_sub += 1
            return total_sub <= k
        
        while l <= r:
            mid = (l + r) // 2
            # print(l, r, mid , is_poss(mid))
            if is_poss(mid):
                r = mid - 1
            else:
                l = mid + 1
        return l