class Solution:
    def maximumEnergy(self, energy: List[int], k: int) -> int:
        res = [0] * len(energy)
        ans = -1001
        for i in range(len(energy)):
            if i - k < 0:
                res[i] = energy[i]
            else:
                res[i] = max(0, res[i-k]) + energy[i]
            if i + k >= len(energy):
                ans = max(ans, res[i])
        return ans
        