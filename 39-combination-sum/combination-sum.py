class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        final_ans = []
        def get_candidates(target, cur_sum, i, cur_vec):
            if cur_sum == target:
                if cur_vec not in final_ans:
                    final_ans.append(cur_vec)
                return
            if i >= len(candidates) or cur_sum > target:
                return
            get_candidates(target, cur_sum + candidates[i], i+1, cur_vec + [candidates[i]])
            get_candidates(target, cur_sum + candidates[i], i, cur_vec + [candidates[i]])
            get_candidates(target, cur_sum + 0, i+1, cur_vec)
            return
        get_candidates(target, 0, 0, [])
        return final_ans
        