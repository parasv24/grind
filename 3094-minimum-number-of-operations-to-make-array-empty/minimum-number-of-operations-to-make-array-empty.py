class Solution:
    def minOperations(self, nums: List[int]) -> int:
        cnt = Counter(nums)
        ans = 0
        for el,val in cnt.items():
            if val == 1:
                return -1
            elif val % 3 == 0:
                ans += val // 3
            else:
                ans += val // 3 + 1
        return ans
