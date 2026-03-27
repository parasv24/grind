class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        def rec(i, arr, total, taken):
            if total > target:
                return
            if i == len(candidates):
                if total == target:
                    ans.append(arr)
                return
            
            rec(i, arr + [candidates[i]], total + candidates[i], 1)
            rec(i+1, arr + [candidates[i]], total + candidates[i], 0)
            if taken == 0:
                rec(i+1, arr, total, 0)
        rec(0, [], 0, 0)
        return ans
        