class Solution:
    def isGood(self, nums: List[int]) -> bool:
        n = len(nums) - 1
        mp = Counter(nums)
        mx = max(nums)
        return sum(nums) == ((n * (n + 1) // 2) + n) and len(mp.keys()) == n and mx == n
        