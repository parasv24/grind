class Solution:
    def maxProduct(self, nums: List[int], k: int, limit: int) -> int:
        n = len(nums)

        # If k is impossible to reach at all
        total_sum = sum(nums)
        if abs(k) > total_sum:
            return -1

        # suffix[i] = sum(nums[i:])
        suffix = [0] * (n + 1)
        for i in range(n - 1, -1, -1):
            suffix[i] = suffix[i + 1] + nums[i]

        @cache
        def rec(i, pre, cur, pro):
            # Prune impossible cur states
            if abs(k - cur) > suffix[i]:
                return -1

            if i == len(nums):
                if cur == k and pro <= limit and pro >= 0:
                    return pro
                else:
                    return -1
            mul = -1 if pre == 1 else 1
            ans = rec(i+1, pre, cur, pro)
            if pro == -2:
                new_pro = nums[i]
            elif pro == -1:
                new_pro = -1 if nums[i] != 0 else 0
            else:
                new_pro = (pro * nums[i])
                new_pro = -1 if new_pro > limit else new_pro
            ans = max(ans, rec(i+1, mul, cur + (mul * nums[i]), new_pro))
            return ans
        return rec(0, -1, 0, -2)
