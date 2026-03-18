class Solution:
    def maximumBeauty(self, nums: List[int], k: int) -> int:
        mp = {}
        for el in nums:
            lower = max(0, el - k)
            higher = min(100000, el + k)
            higher += 1
            mp[lower] = mp.get(lower, 0) + 1
            mp[higher] = mp.get(higher, 0) - 1
        prev = 0
        maxi = -1
        for key in sorted(mp.keys()):
            prev += mp[key]
            maxi = max(maxi, prev)
        return  maxi
