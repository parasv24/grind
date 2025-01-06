class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        mp = Counter({0: 1})
        prev = 0
        total_subs = 0
        for el in nums:
            prev = (prev + el) % k
            total_subs += mp[prev]
            mp[prev] += 1
        return total_subs