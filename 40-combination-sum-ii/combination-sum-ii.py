class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        final_ans = []
        def get_candidates(target, cur_sum, i, cur_vec):
            if cur_sum == target:
                final_ans.append(cur_vec)
                return
            if i >= len(candidates) or cur_sum > target:
                return
            get_candidates(target, cur_sum + candidates[i], i+1, cur_vec + [candidates[i]])
            while i + 1 < len(candidates) and candidates[i] == candidates[i + 1]:
                i += 1
            get_candidates(target, cur_sum + 0, i+1, cur_vec)
            return
        get_candidates(target, 0, 0, [])
        return final_ans


        