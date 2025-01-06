class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        n = len(nums)
        arr = [i - nums[i] for i in range(0, len(nums))]
        mp = Counter(arr)
        cnt = 0
        for x, y in mp.items():
            if y > 1:
                cnt += (y * (y-1)) // 2
        return (n * (n-1)) // 2 - cnt