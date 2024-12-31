class Solution:
    def minimumLevels(self, possible: List[int]) -> int:
        sm = sum(possible)
        zeroes = len(possible) - sm
        final_sm = sm - zeroes
        cur_sum = 0
        for i in range(len(possible)-1):
            cur_sum += 1 if possible[i] == 1 else -1
            if cur_sum > final_sm - cur_sum:
                return i + 1
        return -1



        