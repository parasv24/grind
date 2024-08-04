class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        all_subs_sums = []
        for i in range(0, len(nums)):
            sums = 0
            for j in range(i, len(nums)):
                sums += nums[j]
                all_subs_sums.append(sums)
        all_subs_sums.sort()
        ans = 0
        for i in range(left - 1, right):
            ans += all_subs_sums[i]
        return ans % 1000000007
        