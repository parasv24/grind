class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        total_sum = sum(skill)
        sm = total_sum * 2 // len(skill)
        if sm * len(skill) // 2 != total_sum:
            return -1
        mp = defaultdict(int)
        ans = 0
        pairs = 0
        for val in skill:
            if mp[sm - val] > 0:
                ans += val * (sm - val)
                pairs += 1
                mp[sm-val] -= 1
            else:
                mp[val] += 1
        return ans if pairs == len(skill) // 2 else -1
        