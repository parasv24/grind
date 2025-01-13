class Solution:
    def minimumLength(self, s: str) -> int:
        mp = Counter(list(s))
        final_mp = {}
        left_cnt = {}
        for el in s:
            left = left_cnt.get(el, 0)
            right = mp[el] - left - 1
            final_mp[el] = min(final_mp.get(el, 100000), abs(right - left) + 1)
            left_cnt[el] = left_cnt.get(el, 0) + 1
        return sum(final_mp.values())
        